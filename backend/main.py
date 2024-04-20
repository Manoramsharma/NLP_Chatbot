from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import db_helper
import generic_helper

app = FastAPI()

@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract the necessary information from the payload
    # based on the structure of the WebhookRequest from Dialogflow
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
    session_id = generic_helper.extract_session_id(output_contexts[0]["name"])

    intent_handler_dict = {
        'job.inquiry': job_inquiry,
        'event.eligibility': event_eligibility,
        'event.progress': event_progress,
        'personalized.recommendations': personalized_recommendations,
        'track.registration': track_registration,
        'check.event.details': check_event_details
    }

    return intent_handler_dict[intent](parameters, session_id)

def job_inquiry(parameters: dict, session_id: str):
    job_type = parameters.get("job_type")
    job_listings = db_helper.fetch_job_listings(job_type)
    if job_listings:
        job_listing_texts = [f"{job['title']} at {job['company']}" for job in job_listings]
        fulfillment_text = "Here are some job listings: " + ", ".join(job_listing_texts)
    else:
        fulfillment_text = "Sorry, I couldn't find any job listings matching your criteria."

    return JSONResponse(content={"fulfillmentText": fulfillment_text})

def event_eligibility(parameters: dict, session_id: str):
    event_name = parameters.get("event_name")
    eligibility = generic_helper.check_eligibility(session_id, event_name)
    if eligibility:
        fulfillment_text = f"You are eligible to participate in {event_name}."
    else:
        fulfillment_text = f"Sorry, you do not meet the eligibility criteria for {event_name}."

    return JSONResponse(content={"fulfillmentText": fulfillment_text})

def event_progress(parameters: dict, session_id: str):
    event_name = parameters.get("event_name")
    progress = db_helper.get_event_progress(session_id, event_name)
    fulfillment_text = f"Your current progress for {event_name} is: {progress}."

    return JSONResponse(content={"fulfillmentText": fulfillment_text})

def personalized_recommendations(parameters: dict, session_id: str):
    recommendations = db_helper.get_recommendations(session_id)
    fulfillment_text = f"Based on your profile, we recommend: {recommendations}."

    return JSONResponse(content={"fulfillmentText": fulfillment_text})

def track_registration(parameters: dict, session_id: str):
    event_name = parameters.get("event_name")
    registration_status = db_helper.check_user_registration(session_id, event_name)
    fulfillment_text = "You are currently registered." if registration_status else "You are not registered yet."

    return JSONResponse(content={"fulfillmentText": fulfillment_text})

def check_event_details(parameters: dict, session_id: str):
    event_name = parameters.get("event_name")
    event_details = db_helper.fetch_event_details(event_name)
    if event_details:
        fulfillment_text = f"Event {event_name} details: {event_details}."
    else:
        fulfillment_text = f"Details for {event_name} are not available right now."

    return JSONResponse(content={"fulfillmentText": fulfillment_text})
