from django.shortcuts import redirect, render, get_object_or_404
from .models import Recipe, RecipeIngredients
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm, RecipeIngredientsForm
from django.forms.models import modelformset_factory
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

# old for reference
@login_required
def recipe_update_view_old(request, id=None):
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
        form.save(commit=False)
        form_2.save(commit=False)
        print("form", form.cleaned_data)
        # how to save this 2 form together, not best way:
        parent = form.save(commit=False)
        parent.save()
        child = form_2.save(commit=False)
        child.recipe = parent
        child.save()
        context['message'] = 'Data saved.'
    return render(request, "recipies/create-update.html", context)

# base on 61 - Manage QuerySets with Django Formsets + modelformset factory
# not the best way we will use later on mode correctly
@login_required
def recipe_update_view_old2(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    # instance obj is fullfilling form with specific data(in this case data from specific obj we entered to edit)
    form = RecipeForm(request.POST or None, instance=obj)
    form_2 = RecipeIngredientsForm(request.POST or None)
    ingredient_forms = []
    for ingredient_obj in obj.ingredients_set.all():
        ingredient_forms.append(RecipeIngredientsForm(request.POST or None, instance=ingredient_obj))
    context = {
        "form": form,
        "ingredient_forms": ingredient_forms,
        "object": obj
    }
    my_forms = all([form.is_valid() for form in ingredient_forms])
    if my_forms and form.is_valid():
        parent = form.save(commit=False)
        parent.save()
        for form_2 in ingredient_forms:
            child = form_2.save(commit=False)
            child.recipe = parent
            child.save()
        context['message'] = 'Data saved.'
    return render(request, "recipies/create-update.html", context)

# view using modelformset_factory agregate main obj and correlated object related by ForeignKey
@login_required
def recipe_update_view_old3(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    # instance obj is fullfilling form with specific data(in this case data from specific obj we entered to edit)
    form = RecipeForm(request.POST or None, instance=obj)
    # Formset = modelformset_factory(Model, form=ModelForm, extra=0)
    qs = obj.recipeingredients_set.all()
    RecipeIngredientsFormset = modelformset_factory(RecipeIngredients, form=RecipeIngredientsForm, extra=0)
    formset = RecipeIngredientsFormset(request.POST or None, queryset=qs)
    context = {
        "form": form,
        "formset": formset,
        "object": obj
    }
    if all([form.is_valid(), formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        for form in formset:
            child = form.save(commit=False)
            if child.recipe is None:
                child.recipe = parent
            child.save()
        context['message'] = 'Data saved.'
    return render(request, "recipies/create-update.html", context)

@login_required
def recipe_update_view(request, id=None):
    obj = get_object_or_404(Recipe, id=id, user=request.user)
    # instance obj is fullfilling form with specific data(in this case data from specific obj we entered to edit)
    form = RecipeForm(request.POST or None, instance=obj)
    # Formset = modelformset_factory(Model, form=ModelForm, extra=0)
    qs = obj.recipeingredients_set.all()
    RecipeIngredientsFormset = modelformset_factory(RecipeIngredients, form=RecipeIngredientsForm, extra=0)
    formset = RecipeIngredientsFormset(request.POST or None, queryset=qs)
    context = {
        "form": form,
        "formset": formset,
        "object": obj
    }
    if request.method == "POST":
         print(request.POST)
    if all([form.is_valid(), formset.is_valid()]):
        parent = form.save(commit=False)
        parent.save()
        for form in formset:
            child = form.save(commit=False)
            child.recipe = parent
            child.save()
        context['message'] = 'Data saved.'
    return render(request, "recipies/create-update.html", context)