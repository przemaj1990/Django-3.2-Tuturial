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