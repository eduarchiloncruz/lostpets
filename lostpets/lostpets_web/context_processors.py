from lostpets_web.forms import AvatarFormulario
from lostpets_web.models import Avatar


def avatar_context(request):
    avatar_url = None

    if request.user.is_authenticated:
        # Intentar obtener el avatar desde la sesión o la base de datos
        avatar = Avatar.objects.filter(user=request.user).first()
        if avatar and avatar.image:
            avatar_url = avatar.image.url

    return {"avatar_url": avatar_url}

def avatar_context_form(request):
    if request.user.is_authenticated:
        # Obtener el avatar del usuario si existe
        avatar = Avatar.objects.filter(user=request.user).first()
        avatar_url = avatar.image.url if avatar and avatar.image else None
        form_avatar = AvatarFormulario()

        return {"avatar_url": avatar_url, "form_avatar": form_avatar}

    return {}  # Si el usuario no está autenticado, no retorna nada