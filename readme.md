Project Deployed at - https://ugac-project-portal.herokuapp.com/

1) sudo apt update && sudo apt install libldap2-dev libsasl2-dev

# RUNNING ON LOCAL SERVER
1) Download zip and extract it
2) Create .env in root directory
```
EMAIL_ID=<email from which mail is to be sent>
EMAIL_PASSWORD=<password for email>
```
3) Create virtualenv in python using ``virtualenv venv`` and activate it using ``source venv/bin/activate``
4) Now install requirements using ``pip install -r requirements.txt``
5) Now project is ready to run just do ``python manage.py runserver``
