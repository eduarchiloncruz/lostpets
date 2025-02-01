from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from lostpets_web.models import Pet, Avatar
from lostpets_web.forms import (
    PetForm,
    UserRegistrationForm,
    AvatarFormulario,
    UserEditForm,
)
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def home(request):
    if request.method == "POST":
        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            user = request.user

            # Eliminar el avatar anterior si existe
            avatar = Avatar.objects.filter(user=user).first()
            if avatar:
                avatar.delete()

            # Crear un nuevo avatar
            avatar = Avatar.objects.create(
                user=user, image=formulario.cleaned_data.get("image")
            )

            # Guardar la URL del avatar en la sesión
            if avatar.image:
                request.session["avatar_url"] = avatar.image.url

            return redirect("lostpets_web:home")

    formulario = AvatarFormulario()
    return render(request, "home.html", {"form": formulario})


def about(request):
    return render(request, "about.html")


def login_view(request):
    if request.user.is_authenticated:
        return redirect("lostpets_web:home")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Aquí usamos la función login importada
                return redirect("lostpets_web:home")
    else:
        form = CustomAuthenticationForm()

    return render(request, "login.html", {"form": form})


def register_view(request):
    if request.user.is_authenticated:
        return redirect("lostpets_web:home")

    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # Autenticar al usuario después del registro
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)

                # # Set URL Avatar to Sessión
                # avatar = Avatar.objects.get_or_create(user=user)[0]

                # if avatar.image:
                #     request.session["avatar_url"] = avatar.image.url

                return redirect("lostpets_web:home")
        else:
            messages.error(request, "Datos incorrectos")

    else:
        form = UserRegistrationForm()

    return render(request, "register.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("lostpets_web:home")


def pets(request):
    pets = Pet.objects.all()
    return render(request, "pets.html", {"pets": pets})


def pet_detail(request, pk):
    pet = get_object_or_404(Pet, pk=pk)
    return render(request, "petdetail.html", {"pet": pet})


@login_required
def post(request):
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            page = form.save(commit=False)
            page.owner = request.user
            page.save()
            return redirect("lostpets_web:pets")
    else:
        form = PetForm()
    return render(request, "post.html", {"form": form})


@login_required
def pet_update(request, pk):
    # Obtén la mascota por su pk
    pet = get_object_or_404(Pet, pk=pk)

    # Permitir el acceso solo si el usuario es el propietario o un superusuario
    if request.user != pet.owner and not request.user.is_superuser:
        return HttpResponseForbidden("No tienes permisos para editar esta mascota.")

    if request.method == "POST":
        form = PetForm(request.POST, request.FILES, instance=pet)
        if form.is_valid():
            form.save()
            return redirect("lostpets_web:pets")
    else:
        form = PetForm(instance=pet)

    return render(request, "post.html", {"form": form})


@login_required
def profile_edit(request):
    usuario = request.user

    if request.method == "POST":
        formulario = UserEditForm(request.POST)
        print(f"editar_perfil -- POST")
        if formulario.is_valid():
            informacion = formulario.cleaned_data

            print(f"email: {informacion.get("email")}")
            usuario.email = informacion.get("email")
            print(f"last_name: {informacion.get("last_name")}")
            usuario.last_name = informacion.get("last_name")
            print(f"first_name: {informacion.get("first_name")}")
            usuario.first_name = informacion.get("first_name")

            print(f"password1: {informacion.get("password1")}")

            usuario.save()

            return redirect("lostpets_web:home")

    print(f"editar_perfil -- GET")
    formulario = UserEditForm(
        initial={
            "first_name": usuario.first_name,
            "last_name": usuario.last_name,
            "email": usuario.email,
        }
    )

    # Se quitan las Passwords para que no se cambien
    # formulario.fields.pop('password1', None)
    # formulario.fields.pop('password2', None)

    return render(request, "profile_edit.html", {"form": formulario})


@login_required
def pet_delete(request, pk):
    print(request, pk)
    pet = get_object_or_404(Pet, pk=pk, owner=request.user)
    if request.method == "POST":
        pet.delete()
        return redirect("lostpets_web:home")
    return render(request, "pets.html", {"pet": pet})


from django.contrib.auth.forms import AuthenticationForm
from django import forms


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control my-3 ms-2"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control my-3 ms-2"})
    )
