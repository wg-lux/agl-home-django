# runserver.py
import subprocess

def start_django():
    subprocess.run(["python", "agl_home_django/manage.py", "makemigrations"])
    subprocess.run(["python", "agl_home_django/manage.py", "migrate"])
    subprocess.run(["python", "agl_home_django/manage.py", "runserver"])