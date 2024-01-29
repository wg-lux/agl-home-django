# runserver.py
import subprocess

# Change path? /lib/python3.11/site-packages/agl_home_django

def start_django():
    # subprocess.run(["python", "/home/agl-admin/agl-home-django/agl_home_django/manage.py", "makemigrations"])
    # subprocess.run(["python", "/home/agl-admin/agl-home-django/agl_home_django/manage.py", "migrate"])
    # subprocess.run(["python", "/home/agl-admin/agl-home-django/agl_home_django/manage.py", "runserver"])

    subprocess.run(["python", "manage.py", "makemigrations"])
    subprocess.run(["python", "manage.py", "migrate"])
    subprocess.run(["python", "manage.py", "runserver"])