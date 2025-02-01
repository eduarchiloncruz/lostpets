# lostpets_web/forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Pet


## Seccion Usuario
class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(
        label="Nombre de Usuario",
        widget=forms.TextInput(attrs={"class": "form-control my-3 ms-2"}),
        max_length=30,
        required=True,
    )
    email = forms.EmailField(
        label="Correo Electrónico",
        widget=forms.EmailInput(attrs={"class": "form-control my-3 ms-2"}),
        max_length=254,
        required=True,
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control my-3 ms-2"}),
        required=True,
    )
    password2 = forms.CharField(
        label="Confirmar Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control my-3 ms-2"}),
        required=True,
    )
    last_name = forms.CharField(
        label="Apellido",
        widget=forms.TextInput(attrs={"class": "form-control my-3 ms-2"}),
        max_length=30,
        required=True,
    )
    first_name = forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={"class": "form-control my-3 ms-2"}),
        max_length=30,
        required=True,
    )

    class Meta:
        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "password1",
            "password2",
        ]


## Seccion Pets


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ["name", "race", "content", "image"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control my-3 ms-2"}),
            "race": forms.TextInput(attrs={"class": "form-control my-3 ms-2"}),
            "content": forms.Textarea(
                attrs={"class": "form-control my-3 ms-2", "rows": 4}
            ),
            "image": forms.ClearableFileInput(
                attrs={"class": "form-control my-3 ms-2"}
            ),
        }
        labels = {
            "name": "Nombre",
            "race": "Raza",
            "content": "Descripción",
            "image": "Imagen",
        }


class AvatarFormulario(forms.Form):
    image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={"class": "form-control  my-3 ms-2"})
    )


class UserEditForm(forms.Form):
    email = forms.EmailField(
        label="Ingresar email",
        widget=forms.EmailInput(attrs={"class": "form-control  my-3 ms-2"}),
    )
    password1 = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control  my-3 ms-2"}),
    )
    password2 = forms.CharField(
        label="Repetir Contraseña",
        widget=forms.PasswordInput(attrs={"class": "form-control  my-3 ms-2"}),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control  my-3 ms-2"})
    )
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control  my-3 ms-2"})
    )

    class Meta:
        model = User
        fields = ["email", "password1", "password2", "last_name", "first_name"]
