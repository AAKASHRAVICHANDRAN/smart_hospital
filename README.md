# Smart Hospital (Django-only)

## Setup (Windows / macOS / Linux)
1. Create venv & activate
   python -m venv .venv
   # Windows:
   .\.venv\Scripts\activate
   # macOS / Linux:
   source .venv/bin/activate

2. Install requirements
   pip install -r requirements.txt

3. Create migrations & migrate
   cd smart_hospital
   python ../manage.py makemigrations
   python ../manage.py migrate

4. Create superuser
   python ../manage.py createsuperuser

5. Run the server
   python ../manage.py runserver

Open http://127.0.0.1:8000/
- Home page: /
- Admin: /admin/
- Login: /accounts/login/
