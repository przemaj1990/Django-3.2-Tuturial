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

# 16 - Rendering Data from our Database in a View - Python & Django 3.2 Tutorial Series
    use data from model/database inside django template
    def using_model:
    articles_obj = Article.objects.get(id=4)

# 17 - Django Templates Basics - Python & Django 3.2 Tutorial Series
    > If you would like to use folder with tempalte in django, you need to add it in settings.py
        in TEMPLATES: 
            'DIRS': ['/home/pm1990/Django-3.2-Tuturial/templates']
        and this is most basic and incorrect way
        you can add many of them and django will check them in order you choosed:
            'DIRS': [
                    '/home/pm1990/Django-3.2-Tuturial/templates',
                    '/home/pm1990/Django-3.2-Tuturial/templates2'
                    ],
        but correct way is to add:
            'DIRS': [
                BASE_DIR / "templates"] <- this way we are not point your own system but more general one hierarchy
    > Rednering template:
        we cam use: from django.template.loader import render_to_string
        to use django build in mechanism like that: 
            html_strinh = render_to_string("using_template-view.html", context=context_dict)
        and pass there template html file and context dict as well. 
    - In template use double brackets: <p1>Content: {{content}} </p1
    - Other way is to use get_template module (example def using_template2)
    > Template inheritance:
        at start of tempalte we use {% extends "base.html" %} to use specific base temaple and
         {% block content %}
         {% endblock content %}
        to add our content inside this base.html. this way we connect 2 tempaltes in one website. 

# 18 - Listing Data in Views & Templates - Python & Django 3.2 Tutorial Series
    - We can use for in html using:
        {% for x in my_list %} {{ x }} {% endfor %}
    - Inside we can use {{ x.title }} to get specific value from queryset
    - we can use {% if x.title %}{% endif %} to check if value exist and then render it.
    - we can create link to object by addidng <a href='/articles/{{x.id}}/'>

# 19 - Dynamic URL Routing - Python & Django 3.2 Tutorial Series
    - dynamic url + detail view base on id

# 20 - Super Users, Staff Users & the Django Admin - Python & Django 3.2 Tutorial Series
    - Create super user:
    python3.8 manage.py createsuperuser (pm1990/default password)

# 21 - Register Model in the Admin - Python & Django 3.2 Tutorial Series
    - to manage specific model from admin view you need to add to app_name/admin.py
        admin.site.register(Article)
    - we can add class to display title in admin view insted of object(id) and search using build in mechanism

# 22 - Search Form & Request Data - Python & Django 3.2 Tutorial Series
    > Create basic search form:
     <form action="/articles/">
            <input type='text' name='query'/>
            <input type='submit'/>
    </form>
    that will use def article_search_view()

# 23 - Basic HTML Form in Django - Python & Django 3.2 Tutorial Series
    - @csrf_exempt - decorator in view def allow to avoide problem with csrf token
    - or we can add {% csfr_token %} in create.html
    - base method to add data: Article.objects.create(title=title, content=content)
    using POST request

# 24 - Create a Login View to Authenticate Users - Python & Django 3.2 Tutorial Series
    > authentication methods:
    python3.8 manage.py startapp accounts
    - we add login view
    we will use buildin: from django.contrib.auth import authenticate, login
    user = authenticate(request, username=username, password=password) <- to check if username&password are correct
    login(request, user) <- to login user into admin portal

# 25 - Django Logout View - Python & Django 3.2 Tutorial Series
    - logout mechanism using: from django.contrib.auth import logout

# 26 - Creating a User Required - Python & Django 3.2 Tutorial Series
    > ensure that only log in users are able to edit/see anything, 
    - simple method:
    if request.user.is_authenticate:
        retunr redirect("/login")
    - but is better to use decorator from build in: from django,contrib.auth.decorator import login_required
    @login_required
    - it will redirect us to default website so we need to change this in settings.py:
    LOGIN_URL = "/login/"

# 27 - Basic Django Forms - Python & Django 3.2 Tutorial Series
    > creat article using django forms & add validation
    - we used: form.cleaned_data
    form.cleaned_data returns a dictionary of validated form input fields and their values, where string primary keys are returned as objects.

# 28 - Model Form for Article Model - Python & Django 3.2 Tutorial Series
    - more clear usage of form 

# 29 - Register a User via built in Model Form - Python & Django 3.2 Tutorial Series
    > build registration view.