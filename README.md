# Django-3.2-Tuturial
    based on: https://www.youtube.com/watch?v=SlHBNXW1rTk&amp;list=PLEsfXFp6DpzRMby_cSoWTFw8zaMdTEXgL

# 1 - Welcome to Try Django 3.2 - Python & Django 3.2 Tutorial Series:
    git clone https://github.com/przemaj1990/Django-3.2-Tuturial.git

# 2 - Demo after 73 Parts - Python & Django 3.2 Tutorial Series:
    - general overview of project

# 3 - Requirements - Python & Django 3.2 Tutorial Series:
    touch requirements.txt
    
# 4 - Python & Python Virtual Environment Setup on macOS - Python & Django 3.2 Tutorial Series
# 5 - Windows
    - A how-to guide for creating a Django project for use in both Local & Production (deployment) environments:
      https://www.codingforentrepreneurs.com/blog/create-a-blank-django-project   

    sudo apt-get update
    sudo apt-get -y upgrade
    python3 -V
    sudo apt-get install -y python3-pip
    sudo apt-get install build-essential libssl-dev libffi-dev python-dev
    sudo apt-get install -y python3-venv
    virtualenv -p python3 .
    (insted we can use python -m venv my_venv )
    source bin/activate
    pip freeze
    pip install -r requirements.txt 
    (pip freeze > requirements.txt to save into requirements)
    pip install --upgrade pip
    git config --global user.email 'przemaj1990@gmail.com'
    git add .
    git commit -m 'first test commit'
    git push

# 6 - Setup a Django Project- Python & Django 3.2 Tutorial Series:

    python -m django
    django-admin
    python -m django startproject trydjango . (create project in this dir)
    python -m django startproject trydjango (create project in dir /trydjango )
    python manage.py

# 7 - Setup Django on VS Code - Python & Django 3.2 Tutorial Series
# 8 - Databases & Web Pages - Python & Django 3.2 Tutorial Series
# 9 - Open, Activate, & Run Dev Server - Python & Django 3.2 Tutorial Series

    - on mac:
    python3.8 -m venv .
    source bin/activate
    - repete steps from #5 & then:
    python3.8 manage.py runserver
    python3.8 manage.py runserver -d (run in a background)
    python manage.py runserver 10.0.85.136:8000

# 10 - Your first web page - Python & Django 3.2 Tutorial Series
# 11 - Handling a url route - Python & Django 3.2 Tutorial Series

    - add views.py and first def to render webpage
    - add 'home/' in urls.py
