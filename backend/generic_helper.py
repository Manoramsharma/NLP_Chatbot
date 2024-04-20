def check_eligibility(user_id, event_name):
    # Assume db_helper has a method to get user info and event requirements
    user_info = db_helper.get_user_info(user_id)
    event_requirements = db_helper.fetch_event_details(event_name)
    # Simple eligibility check based on user level or skills
    return user_info['level'] >= event_requirements['required_level']

def get_personalized_recommendations(user_id):
    # This could use a more complex algorithm or even call an external service
    return db_helper.get_recommendations(user_id)
