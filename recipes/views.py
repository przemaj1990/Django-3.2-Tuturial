from django.shortcuts import redirect, render, get_object_or_404
from .models import Recipe, RecipeIngredients
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm
# Create your views here.

# CRUD -> Create, Retrive, Update, Delete

@login_required
def recipe_list_view(request, id=None):
    qs = Recipe.objects.filter(user=request.user)
    context = {
        "object_list": qs
    }
    return render(request, "recipies/list.html", context)

@login_required
def recipe_detail_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    context = {
        "object": obj
    }
    return render(request, "recipies/detail.html", context)

@login_required
def recipe_create_view(request):
    form = RecipeForm(request.POST or None)
    context = {
        "form": form
    }
    if form.is_valid():
        obj = form.save(comit=False)
        obj.user = request.user
        obj.save()
        return redirect(obj.get_absolute_url)
    return render(request, "recipies/create-update.html", context)

@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    form = RecipeForm(request.POST or None, instance=obj)
    context = {
        "form": form,
        "object": obj
    }
    if form.is_valid():
        form.save()
        context['message'] = 'Data saved.'
    return render(request, "recipies/create-update.html", context)