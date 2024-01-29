# runserver.py
import subprocess

# Change path? /lib/python3.11/site-packages/agl_home_django

def start_django():
    subprocess.run(["python", "agl_home_django/manage.py", "makemigrations"])
    subprocess.run(["python", "agl_home_django/manage.py", "migrate"])
    subprocess.run(["python", "agl_home_django/manage.py", "runserver"])