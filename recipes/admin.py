from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Recipe, RecipeIngredients
# Register your models here.

# everywhere (but not in model) we get user model using:
User = get_user_model()

# # we need to logout user to use register then
# admin.site.unregister(User)
# class RecipeInline(admin.StackedInline):
#     model = Recipe
#     extra = 0
# #allow to overwrite users view to put there adding recipies there
# class UserAdmin(admin.ModelAdmin):
#     inlines = [RecipeInline]
#     list_display = ['username']

# admin.site.register(User, UserAdmin)


class RecipeIngredientsInline(admin.StackedInline):
    model = RecipeIngredients
    extra = 0
    # fields = ['name', 'quantity', 'unit', 'directions']

class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientsInline]
    list_display = ['name', 'user']
    readonly_fields = ['timestamp', 'updated']
    #add lookup to search user
    raw_id_fields = ['user']

# admin.site.register(RecipeIngredients)

admin.site.register(Recipe, RecipeAdmin)