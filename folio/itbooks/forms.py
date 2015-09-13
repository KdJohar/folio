from django import forms
from .models import SearchTag
class SearchForm(forms.ModelForm):
    search = forms.CharField(max_length=250)
    class Meta:
        model = SearchTag
        fields = ['search']
