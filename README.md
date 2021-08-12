# Closest Points App
A python Django application that calculates the closest points pair from a comma separated string like "(2,3), (1,1), (5, 4),..."

# Requirements
1. Python3
2. SQLite (MySQL or Postgres also fine)

# Installation
1. Start and activate a new python virtual environment: `python3 -m venv myprojectfolder`
2. Clone this repository: `git clone https://github.com/collinspamba/closest-points.git myprojectfolder`
3. Create a `local.py` file inside the closestpoints/ folder and add the following settings:
    1. `SECRET_KEY = 'your random secret key here'`
    2. `Debug = True` # only in development!
    3. `ALLOWED_HOSTS = ['127.0.0.1']` # for use with django's builtin web server: `python manage.py runserver`
4. Install external packages: run `pip install -r requirements.txt` in the project root.
5. Start the app using `python manage.py runserver`

# Documentation
See https://closestpoints.buffalo.co.ke
