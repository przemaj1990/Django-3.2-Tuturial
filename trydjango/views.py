# tu render html web page
from django.http import HttpResponse
import random

# simple response:
def simple_response(request):
    name = 'Przemek'
    random_nr = random.randint(1,10000)
    html_strinh1 = f"""<h1>Hello {name}</h1>"""
    html_strinh2 = f"""<p1>Test uzycia p1 : {random_nr} </p1>"""
    html_strinh = html_strinh1 + html_strinh2
    # take request and retun respone 
    return HttpResponse(html_strinh)

# django template: