# tu render html web page
from django.http import HttpResponse

# 10 - Your first web page - Python & Django 3.2 Tutorial Series
def home(request):
    html_strinh = """<h1>Hello World</h1>"""

    # take request and retun respone 
    return HttpResponse(html_strinh)