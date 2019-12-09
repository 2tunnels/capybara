from django import forms


class AuthorizeForm(forms.Form):
    subdomain = forms.CharField(max_length=100)
