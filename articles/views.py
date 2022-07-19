from django.shortcuts import render
from .models import Article
# Create your views here.

#handling dynamic url & detail view
def article_detail_view(request, id=None):
    articles_obj = Article.objects.get(id=id)
    context = {
        "object": articles_obj,
        }
    # render allow us to paste request, template and context
    return render(request, "articles/detail.html", context=context)

def article_search_view(request):
    #to print detail of request:
    # print(dir(request))
    # print(request.GET)
    query_dict = request.GET #this is dict
    query = query_dict.get('query')
    try:
        query = int(query_dict.get('query'))
    except:
        query = None
    articles_obj = None
    if query is not None:
        #base search:
        articles_obj = Article.objects.get(id=query)
    context = {
        "object": articles_obj,
        }
    return render(request, "articles/search.html", context=context)