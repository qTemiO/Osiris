from django import forms

class NewsCollectForm(forms.Form):
    url = forms.URLField()

class TabsCollectForm(forms.Form):
    url = forms.URLField()