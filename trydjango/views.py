# tu render html web page
from django.http import HttpResponse
import random
from articles.models import Article
from django.template.loader import render_to_string, get_template
# simple response:
def simple_response(request):
    name = 'Przemek'
    random_nr = random.randint(1,10000)
    html_strinh1 = f"""<h1>Hello {name}</h1>"""
    html_strinh2 = f"""<p1>Test uzycia p1 : {random_nr} </p1>"""
    html_strinh = html_strinh1 + html_strinh2
    # take request and retun respone 
    return HttpResponse(html_strinh)

# base django template:
def using_model(request):
    # get data from databse
    articles_obj = Article.objects.get(id=4)
    # django template
    html_strinh1 = f"""<h1> {articles_obj.title} (id: {articles_obj.id}) </h1>"""
    html_strinh2 = f"""<p1> {articles_obj.content} </p1>"""
    html_strinh = html_strinh1 + html_strinh2
    return HttpResponse(html_strinh)

# using format method, 
def using_format(request):
    articles_obj = Article.objects.get(id=3)
    context_dict = {
        "title": articles_obj.title,
        "id": articles_obj.id,
        "content": articles_obj.content }
    # we use (**context_dict) to unpack dict context_dict inside format
    html_strinh1 = """<h1> Title: {title} id: {id} </h1><p1>{content}</p1> """.format(**context_dict)
    return HttpResponse(html_strinh1)

def using_template1(request):
    articles_obj = Article.objects.get(id=4)
    context_dict = {
        "title": articles_obj.title,
        "id": articles_obj.id,
        "content": articles_obj.content }
    html_strinh = render_to_string("using_template-view.html", context=context_dict)
    return HttpResponse(html_strinh)

def using_template2(request):
    articles_obj = Article.objects.get(id=3)
    context_dict = {
        "title": articles_obj.title,
        "id": articles_obj.id,
        "content": articles_obj.content }
    template = get_template("using_template-view.html")
    template_str = template.render(context=context_dict)
    return HttpResponse(template_str)