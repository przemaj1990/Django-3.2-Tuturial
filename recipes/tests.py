from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
# Create your tests here.
from .models import Recipe, RecipeIngredients

User = get_user_model()

class UserTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('pm_test', password='abc123')
        self.recipe_a = Recipe.objects.create(
            name='Grilled Chicken',
            user = self.user_a
        )

    def test_user_password(self):
        checked = self.user_a.check_password('abc123')
        self.assertTrue(checked)

class RecipeTestCase(TestCase):
    def setUp(self):
        self.user_a = User.objects.create_user('cfe', password='abc123')
        self.recipe_a = Recipe.objects.create(
            name='Grilled Chicken',
            user = self.user_a
        )
        self.recipe_b = Recipe.objects.create(
            name='Grilled Chicken Tacos',
            user = self.user_a
        )
        self.recipe_ingredient_a = RecipeIngredients.objects.create(
            recipe=self.recipe_a,
            name='Chicken',
            quantity='1/2',
            unit='pound'
        )
        self.recipe_ingredient_b = RecipeIngredients.objects.create(
            recipe=self.recipe_a,
            name='Chicken',
            quantity='asdfasd',
            unit='pound'
        )
    
    def test_user_count(self):
        qs = User.objects.all()
        self.assertEqual(qs.count(), 1)

    def test_user_recipe_reverse_count(self):
        user = self.user_a 
        qs = user.recipe_set.all() 
        self.assertEqual(qs.count(), 2)

    def test_user_recipe_forward_count(self):
        user = self.user_a 
        qs = Recipe.objects.filter(user=user)
        self.assertEqual(qs.count(), 2)

    def test_recipe_ingredient_reverse_count(self):
        recipe = self.recipe_a 
        qs = recipe.recipeingredients_set.all() 
        self.assertEqual(qs.count(), 2)

    def test_recipe_ingredientcount(self):
        recipe = self.recipe_a 
        qs = RecipeIngredients.objects.filter(recipe=recipe)
        self.assertEqual(qs.count(), 2)

    def test_user_two_level_relation(self):
        user = self.user_a
        qs = RecipeIngredients.objects.filter(recipe__user=user)
        self.assertEqual(qs.count(), 2)

    def test_user_two_level_relation_reverse(self):
        user = self.user_a
        recipeingredients_ids = list(user.recipe_set.all().values_list('recipeingredients__id', flat=True))
        qs = RecipeIngredients.objects.filter(id__in=recipeingredients_ids)
        self.assertEqual(qs.count(), 2)

    def test_unit_measure_validation(self):
        invalid_unit = 'ounce'
        ingredient = RecipeIngredients(
            name='New',
            quantity=10,
            recipe=self.recipe_a,
            unit=invalid_unit
        )
        ingredient.full_clean()

    def test_unit_measure_validation_error(self):
        invalid_units = ['nada', 'asdfadsf']
        with self.assertRaises(ValidationError):
            for unit in invalid_units:
                ingredient = RecipeIngredients(
                    name='New',
                    quantity=10,
                    recipe=self.recipe_a,
                    unit=unit
                )
                ingredient.full_clean()

    # def test_quantity_as_float(self):
    #     self.assertIsNotNone(self.recipe_ingredient_a.quantity_as_float)
    #     self.assertIsNone(self.recipe_ingredient_b.quantity_as_float)