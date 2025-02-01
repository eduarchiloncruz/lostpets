from django.urls import path
from django.contrib import admin
from lostpets_web.views import (
    home,
    about,
    login_view,
    register_view,
    pets,
    post,
    logout_view,
    pet_detail,
    pet_update,
    profile_edit,
    pet_update,
    pet_delete,
)
from django.contrib.auth import views as auth_views

app_name = "lostpets_web"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("home/", home, name="home"),
    path("about/", about, name="about"),
    path("pets/", pets, name="pets"),
    path("pets/<int:pk>/", pet_detail, name="petdetail"),
    path("post/", post, name="post"),
    path("pets/<int:pk>/delete/", pet_delete, name="pet_delete"),
    path("post/<int:pk>/edit/", pet_update, name="pet_update"),
    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
    path("profile/", profile_edit, name="profile"),
]
