# TalentTalk: A NLP based interactive chatbot 🤖💼

Welcome to **TalentTalk**, your intelligent companion in the realm of recruitment and talent acquisition. TalentTalk is designed to bridge the gap between job seekers and their next big opportunity. From hackathons to job openings, TalentTalk is your go-to guide for navigating the professional world.

## Features ✨

- **Job Inquiries** 🕵️‍♂️: Access a wide range of job listings that match your skillset.
- **Event Information** 📅: Receive updates and details on industry events, hackathons, and contests.
- **Eligibility Checks** ✔️: Instantly check your eligibility for the events and jobs you're interested in.
- **Progress Tracking** 📈: Monitor your application status and event participation milestones.
- **Personalized Recommendations** 🔍: Get curated job and event suggestions tailored to your experiences.
- **Registration Status** 📝: Easily check your sign-up details for upcoming events.
- **Preparation Tips** 📘: Find resources and advice to prepare for various competition rounds and job interviews.

## Technologies and Techniques 🛠️

TalentTalk is powered by state-of-the-art technology and innovative techniques in the field of AI and NLP:

- **Dialogflow**: Utilizes Google's Dialogflow for natural language understanding and intent recognition.
- **FastAPI**: Built with FastAPI for high-performance backend services, enabling async request handling.
- **MySQL**: Integrates with MySQL for robust data storage and retrieval, ensuring consistent tracking and updates.
- **Machine Learning**: Employs machine learning algorithms for continuous improvement based on user interactions.
- **Cloud Services**: Hosted on cloud platforms for scalability, reliability, and 24/7 availability.
- **Personalization Engines**: Incorporates personalization engines to tailor recommendations and responses.

## Setup and Installation 🛠️

To get TalentTalk up and running on your local machine, follow these steps:

### Prerequisites

Ensure you have the following installed:
- [Python](https://www.python.org/downloads/) (version 3.7 or later)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [MySQL](https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/)

### Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Manoramsharma/NLP_Chatbot.git
    cd talenttalk
    ```

2. **Set up a virtual environment:**
    ```bash
    python -m venv venv
    ```

    For Unix or MacOS, run:
    ```bash
    source venv/bin/activate
    ```

    For Windows, run:
    ```bash
    .\venv\Scripts\activate
    ```

3. **Install the dependencies:**
    ```bash
    pip install -r backend/requirements.txt
    ```

### Database Configuration

1. **Create the MySQL database and user:**
    ```sql
    CREATE DATABASE talent_acquisition_platform;
    CREATE USER 'talenttalk_user'@'localhost' IDENTIFIED BY 'password';
    GRANT ALL PRIVILEGES ON talent_acquisition_platform.* TO 'talenttalk_user'@'localhost';
    FLUSH PRIVILEGES;
    ```

2. **Initialize the database:**
    ```bash
    mysql -u talenttalk_user -p talent_acquisition_platform < path_to_sql_file.sql
    ```

### Running the Application

1. **Start the FastAPI server:**
    ```bash
    uvicorn backend.main:app --reload
    ```

    The `--reload` flag enables live reloading during development.

2. **Access the application:**

    Visit `http://127.0.0.1:8000` in your web browser to see the running application.

You're all set! TalentTalk is now ready to assist users with their recruitment and career advancement queries.

## Get Started 🚀

Just say 'Hello' to begin interacting with TalentTalk. Here are some examples to get you started:

- "What are the latest job openings for a UI/UX designer?"
- "Am I eligible to participate in the annual Tech Innovate Hackathon?"
- "How's my application doing for the Junior Developer position?"
- "Recommend some events based on my profile."
