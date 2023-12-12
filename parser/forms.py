from django import forms


class ParserForm(forms.Form):
    url = forms.URLField(label="Ranobelib URL: ")


class SearchForm(forms.Form):
    title = forms.CharField(max_length=500)
