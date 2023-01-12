Homework
"налаштувати SMTP, та створити шаблони для імейлу по відновленню пароля"

Local setup

Create python environment
$ python3 -m venv .venv

Activate python environment
$ source .venv/bin/activate

Install dependencies
$ pip install -r requirements.txt

Rename file .env.example in .env
Change configuration SMTP server (MAIL_SERVER), port (MAIL_PORT), username (MAIL_USERNAME) and password (MAIL_PASSWORD)
in .env file. Change sander email in file auth.py (line 99) on your email address.  

Run database container
$ docker-compose up -d db

Run app
$ flask run
