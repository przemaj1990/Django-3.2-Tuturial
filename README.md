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

# 12 - Enriching a View with Data - Python & Django 3.2 Tutorial Series
# 13 - Our first database model - Python & Django 3.2 Tutorial Series
    - start app is more like start part of app than app itself
    python3.8 manage.py startapp articles
    - add base model

# 14 - INSTALLED_APPS & Migrations - Python & Django 3.2 Tutorial Series
    python3.8 manage.py migrate
    - it will create 'db.sqlite3' database
    - check {projectname}/settings.py & add new created app into INSTALLED_APPS
    - to make django know about new models we need to(run this every time when you change anything):
    python3.8 manage.py makemigrations
    python3.8 manage.py migrate
    - in {projectname}/{app}/migrations you can find each migration and what was done
    
# 15 - Writing & Reading data in Python Shell - Python & Django 3.2 Tutorial Series
    pip install dataclasses
    python3.8 manage.py shell
    - in django shell we can access already created obj like articles
    >>> from articles.models import Article
    >>> obj = Article()
    >>> obj.title
    ''
    >>> obj.save()
    >>> obj = Article(title='First test article', content='hello')
    >>> obj.save()
    >>> obj.title
    'First test article'
    >>> obj2 = Article(title='Second test article', content='hello')
    >>> obj2.save()
    >>> obj3 = Article.objects.create(title='third test article', content='hello')
    >>> obj3.title
    'third test article'
    >>> a = Article.objects.get(id=2)
    >>> a.title
    'First test article'
    Ctrl + D to close

