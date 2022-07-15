# tu render html web page
from django.http import HttpResponse
import random
from articles.models import Article
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
def using_model(request):
    # get data from databse
    articles_obj = Article.objects.get(id=4)
    # django template
    html_strinh1 = f"""<h1> {articles_obj.title} (id: {articles_obj.id}) </h1>"""
    html_strinh2 = f"""<p1> {articles_obj.content} </p1>"""
    html_strinh = html_strinh1 + html_strinh2
    return HttpResponse(html_strinh)