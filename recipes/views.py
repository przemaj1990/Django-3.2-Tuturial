from django.shortcuts import redirect, render, get_object_or_404
from .models import Recipe, RecipeIngredients
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, RecipeIngredientsForm
# Create your views here.

# CRUD -> Create, Retrive, Update, Delete
# Function Base View:

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
    # instance obj is fullfilling form with specific data(in this case data from specific obj we entered to edit)
    form = RecipeForm(request.POST or None, instance=obj)
    form_2 = RecipeIngredientsForm(request.POST or None)
    context = {
        "form": form,
        "form_2": form_2,
        "object": obj
    }
    if all([form.is_valid(), form_2.is_valid()]):
        # 2 sepearate form for recipes and ingredient
        # form.save(commit=False)
        # form_2.save(commit=False)
        # print("form", form.cleaned_data)
        
        # how to save this 2 form together, not best way:
        parent = form.save(commit=False)
        parent.save()
        child = form_2.save(commit=False)
        child.recipe = parent
        child.save()
        context['message'] = 'Data saved.'
    return render(request, "recipies/create-update.html", context)