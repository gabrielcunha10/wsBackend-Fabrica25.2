from django import forms
from .models import Cadastro
from django.contrib.auth.hashers import make_password

class CadastroForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = Cadastro
        fields = ['nome','sobrenome','cpf','rg','email','senha']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.senha = make_password(self.cleaned_data["senha"])
        if commit:
            user.save()
        return user