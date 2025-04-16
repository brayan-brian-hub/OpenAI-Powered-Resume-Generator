# AI-Powered Resume Generator

This is a simple Flask web application that uses the OpenAI API to generate a resume based on user-provided details. The tool demonstrates API integration and web development, making it a great portfolio project for showcasing your API integration skills.

## Features

- **User Input Form:** Allows the user to enter resume details (job title, skills, etc.).
- **API Integration:** Sends the input as a prompt to the OpenAI API to generate a resume.
- **Result Display:** Renders the generated resume on a results page.

## Requirements

- Python 3.x
- An OpenAI API key (set as the environment variable `OPENAI_API_KEY`)

## Setup & Run

1. **Clone the repository:**

   ```bash
   git clone https://github.com/brayan-brian-hub/ai_resume_generator.git
   cd ai_resume_generator
2.	Install dependencies:
   pip install -r requirements.txt
3.	Set your OpenAI API key:
On Linux/Mac:
   export OPENAI_API_KEY="your-api-key"
On Windows:
set OPENAI_API_KEY=your-api-key
4.	Run the application:
   python app.py
5.	Visit the application:
Open your web browser and go to http://127.0.0.1:5000.

