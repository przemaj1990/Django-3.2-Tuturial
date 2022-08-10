from django.db import models
from django.conf import settings
from .validators import validate_unit
from .utils import number_str_to_float
import pint
from django.urls import reverse
# Create your models here.

"""
General Idea:
- Global
    - Ingredients
    - Recipes
- User
    - Ingredients
    - Recipes
        - Ingredients
        - Directions for Ingredients
"""

class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=270)
    description = models.TextField(null=True, blank=True)
    directions = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        # return "/panty/recipies/"
        return reverse("recipes:detail", kwargs={"id": self.id})

    def get_hx_url(self):
        return reverse("recipes:hx-detail", kwargs={"id": self.id})

    def get_update_url(self):
        return reverse("recipes:update", kwargs={"id": self.id})

    def get_ingredient_children(self):
        return self.recipeingredients_set.all()

class RecipeIngredients(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=270)
    description = models.TextField(null=True, blank=True)
    quantity = models.CharField(max_length=50)
    quantity_as_float = models.FloatField(blank=True, null=True)
    unit = models.CharField(max_length=50, validators=[validate_unit])
    directions = models.TextField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return self.recipe.get_absolute_url()

    def convert_to_system(self, system='mks'):
        if self.quantity_as_float is None:
            return None
        ureg = pint.UnitRegistry(system=system)
        measurement = self.quantity_as_float * ureg[self.unit]
        # print(measurement)
         #.to_base_units() <- change value to desired one specifiec in 'system'
        return measurement #.to_base_units()

    def to_ounces(self):
        m = self.convert_to_system()
        return m.to('ounces')

    def as_mks(self):
        # meter, kilogram, second
        measurement = self.convert_to_system(system='mks')
        return measurement.to_base_units()

    def as_imperial(self):
        # miles, pounds, seconds
        measurement = self.convert_to_system(system='imperial')
        # measurement.to('pounds') <- to specific one.
        return measurement.to_base_units()


    # use validator inside save of model:
    def save(self, *args, **kwargs):
        qty = self.quantity
        qty_as_float, qty_as_float_sucess = number_str_to_float(qty)
        if qty_as_float_sucess:
            self.quantity_as_float = qty_as_float
        else: 
            self.quantity_as_float = None
        super().save(*args, **kwargs)

# class RecipeImage():
#     recipe = models.ForeignKey(Recipe)
