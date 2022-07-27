from django.shortcuts import render, redirect
from django.http import Http404
from .models import Article
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import ArticleFormOld, ArticleForm
# Create your views here.

#handling dynamic url & detail view
def article_detail_view(request, id=None):
    articles_obj = Article.objects.get(id=id)
    context = {
        "object": articles_obj,
        }
    # render allow us to paste request, template and context
    return render(request, "articles/detail.html", context=context)

def article_detail_view_slug(request, slug=None):
    articles_obj = None
    if slug is not None:
        try:
            articles_obj = Article.objects.get(slug=slug)
        except Article.DoesNotExist:
            raise Http404
        except Article.MultipleObjectsReturned:
            articles_obj = Article.objects.filter(slug=slug).first()
        except:
            raise Http404
    context = {
        "object": articles_obj,
        }
    # render allow us to paste request, template and context
    return render(request, "articles/detail.html", context=context)

#base search:
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

#create new article base:
#@csrf_exempt - allow to avoide problem with ssrf token
@login_required #allow to ensure auth of user
def article_create_view(request):
    # simple method of auth(but is better to use decorator):
    # if request.user.is_authenticate:
    #     retunr redirect("/login")
    context = {}
    # first method
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        articles_obj = Article.objects.create(title=title, content=content)
        # we created object/new article and pass its data to template to use it in dynami url
        context["object"] = articles_obj
        context["created"] = True
    # render allow us to paste request, template and context
    return render(request, "articles/create.html", context=context)

# create article using django forms
@login_required
def article_create_view2(request):
    form = ArticleForm()
    # print(dir(form))
    context = {
        "form": form
    }
    if request.method == "POST":
        form = ArticleFormOld(request.POST)
        context['form'] = form
        if form.is_valid():
            title = form.cleaned_data.get("title")
            content = form.cleaned_data.get("content")
            articles_obj = Article.objects.create(title=title, content=content)
            # we created object/new article and pass its data to template to use it in dynami url
            context["object"] = articles_obj
            context["created"] = True
    # render allow us to paste request, template and context
    return render(request, "articles/create2.html", context=context)

#more clear version, using old form:
@login_required
def article_create_view3(request):
    form = ArticleFormOld(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        title = form.cleaned_data.get("title")
        content = form.cleaned_data.get("content")
        articles_obj = Article.objects.create(title=title, content=content)
        # we created object/new article and pass its data to template to use it in dynami url
        context["object"] = articles_obj
        context["created"] = True
    # render allow us to paste request, template and context
    return render(request, "articles/create2.html", context=context)

# using new form version
@login_required
def article_create_view4(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        articles_obj = form.save()
        context["form"] = ArticleForm()
        # context["created"] = True
        return redirect(articles_obj.get_absolute_url())
        # return redirect('article-detail', slug=articles_obj.slug)
    return render(request, "articles/create2.html", context=context)