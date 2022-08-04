from django import forms
from .models import Recipe, RecipeIngredients

class RecipeForm(forms.ModelForm):
    # will add css class to fileds added automatically using this class
    # in effect the frontend will be easy
    required_css_class = 'required-filed'
    error_css_class = 'error-filed'
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "your own placeholder"}), help_text="help_text_for_name <a href='/contact/'>Contact us!</a>")
    # description = forms.CharField(widget=forms.Textarea(attrs={"rows": 3}))
    class Meta:
        model = Recipe
        fields = ['name', 'description', 'directions']

    def __init__(self, *args, **kwargs):
        # call main function
        super().__init__(*args, **kwargs)
        # loop throw all the fields:
        for filed in self.fields:
            print(filed)
            new_data = {
                "placeholder": f'recipe-{str(filed)}',
                'class': 'form-control'
            }
            self.fields[str(filed)].widget.attrs.update(new_data)
        # way of chaning filed using init:
        # self.fields['name'].label = 'Name haha:'
        # self.fields['name'].widget.attrs.update({"class": "form-control2"})
        self.fields['description'].widget.attrs.update({"rows": '2'})
        self.fields['directions'].widget.attrs.update({"rows": '4'})
        # self.fields['name'].widget.attrs.update(placeholder=f"recipe-{field}")


class RecipeIngredientsForm(forms.ModelForm):
    class Meta:
        model = RecipeIngredients
        fields = ['name', 'quantity', 'unit']