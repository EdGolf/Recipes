from django.forms import ModelForm, CheckboxSelectMultiple

from .models import Recipe, Category


class RecipeForm(ModelForm):
    class Meta:
        model = Recipe
        fields = ('name', 'description', 'ingredients',
                  'steps', 'time', 'image', 'categories')
        widgets = {'categories': CheckboxSelectMultiple(), }


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'slug')
