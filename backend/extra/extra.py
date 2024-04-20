from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import random

app = FastAPI()

@app.post("/")
async def handle_request(request: Request):
    # Retrieve the JSON data from the request
    payload = await request.json()

    # Extract the necessary information from the payload
    # based on the structure of the WebhookRequest from Dialogflow
    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']

    intent_handler_dict = {
        'job.recommendation': handle_job_recommendation,
        'event.participation': handle_event_participation,
        'user.progress.update': handle_user_progress_update
    }

    return intent_handler_dict[intent](parameters)


def handle_job_recommendation(parameters: dict):
    user_background = parameters["user-background"]
    # This would be a more complex logic that considers user background and preferences
    # For demonstration purposes, we provide a static response
    recommended_jobs = ["Software Developer", "Data Analyst", "Product Manager"]
    
    response = {
        "fulfillmentText": f"Based on your background as a {user_background}, we recommend considering positions like: " +
                           ", ".join(recommended_jobs)
    }

    return JSONResponse(content=response)

def handle_event_participation(parameters: dict):
    event_name = parameters["event-name"]
    # Dummy logic to decide if the user can participate in an event
    can_participate = random.choice([True, False])
    participation_response = "You can participate in this event." if can_participate else "You are not eligible for this event right now."

    response = {
        "fulfillmentText": participation_response
    }

    return JSONResponse(content=response)

def handle_user_progress_update(parameters: dict):
    user_id = parameters["user-id"]
    event_name = parameters["event-name"]
    new_progress = parameters["new-progress"]
    # Here you would include logic to update the user's progress in an event
    # This is a placeholder for the actual database update operation
    progress_updated = True  # Simulate update

    update_response = f"Your progress for {event_name} has been updated to {new_progress}." if progress_updated else \
                      "Failed to update your progress. Please try again later."

    response = {
        "fulfillmentText": update_response
    }

    return JSONResponse(content=response)

# Additional routes can be added here for handling other intents or operations.
