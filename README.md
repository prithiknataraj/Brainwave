# Brainwave Learning Platform

This is a web application designed to facilitate online learning through interactive video courses, class scheduling, and student management features.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Usage](#usage)
- [License](#license)
- [Contact](#contact)

## Features
- **User Authentication**: Sign up, log in, and manage user profiles with secure password storage.
- **Course Management**: Video courses on various subjects like Python, JavaScript, Data Science, and Machine Learning.
- **Class Scheduling**: Schedule classes with meeting IDs and notify students via email.
- **Profile Management**: Update user profiles, including personal details and passwords.
- **Test Scoring**: Submit and track scores for multiple-choice quizzes.
- **Email Notifications**: Automatically send class details to all registered students.

## Technologies Used
- **Backend**: Flask, Firebase Firestore, Flask-Mail
- **Frontend**: HTML, CSS, Jinja2 Templates
- **Authentication**: Werkzeug for password hashing
- **Payment Processing**: Stripe (optional)
- **Deployment**: Hosted on Flask server

## Setup Instructions

### Prerequisites
- Python 3.8 or higher
- Firebase Admin SDK credentials JSON file
- Gmail account for sending emails (consider setting up an App Password if using 2FA)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/brainwave-learning-platform.git
    cd brainwave-learning-platform
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up Firebase credentials:
    - Place your Firebase Admin SDK credentials JSON file in the project root.
    - Update the path in the code where Firebase is initialized.

5. Configure Flask-Mail:
    - Set your Gmail username and password in the `app.config` section of `app.py`.

6. Set up Stripe (if required):
    - Add your Stripe API keys in the appropriate section of the code.

## Running the Application

1. Start the Flask development server:
    ```bash
    flask run
    ```

2. Open your browser and navigate to `http://127.0.0.1:5000` to view the application.

## Usage

### User Authentication
- **Sign Up**: New users can sign up by providing their name, email, password, gender, and date of birth.
- **Login**: Users can log in with their email and password.
- **Profile Management**: Logged-in users can update their profile details, including password.

### Course Management
- **Courses**: View and interact with video courses in Python, JavaScript, Data Science, and Machine Learning.
- **Class Scheduling**: Schedule classes and send meeting details to all registered students via email.

### Tests
- **Submit Scores**: Users can take quizzes and submit their scores, which are stored in the session.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contact
If you have any questions or suggestions, feel free to reach out to:
- **Email**: prithik0926@gmail.com
