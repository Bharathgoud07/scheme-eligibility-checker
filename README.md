# Scheme Eligibility Checker (Version 1)

A Django-based web application that helps citizens check their eligibility for government schemes based on profile details and available documents.

## Features
- Profile-based eligibility checking
- Document selection system
- Scheme filtering by category and target group
- Eligibility results with reasons
- Clean UI with step-by-step workflow

## Tech Stack
- Python
- Django
- SQLite
- HTML, CSS, JavaScript

## How to Run Locally

1. Clone the repository
git clone https://github.com/Bharathgoud07/scheme-eligibility-checker.git

2. Navigate into project
cd scheme-eligibility-checker

3. Create virtual environment
python -m venv venv

4. Activate environment
venv\Scripts\activate

5. Install dependencies
pip install -r requirements.txt

6. Run migrations
python manage.py migrate

7. Start server
python manage.py runserver
