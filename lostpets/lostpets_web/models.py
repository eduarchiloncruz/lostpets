from django.db import models
from django.contrib.auth.models import User


# Sección Pet
class Pet(models.Model):
    name = models.CharField(max_length=255)
    race = models.CharField(max_length=1500)
    content = models.TextField()
    image = models.ImageField(upload_to="media")
    published_date = models.DateTimeField(auto_now_add=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# End --> Sección Paginas


# Sección Usuarios
# class UserProfile(models.Model):
#     user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
#     # Agrega campos adicionales si es necesario para tu aplicación

#     def __str__(self):
#         return self.user.username


class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatar", null=True, blank=True)

    def __str__(self):
        return f"{self.user}"


# End --> Sección Usuarios
