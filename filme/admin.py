from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Filme, Episodio, Usuario

# só existe porque agente quer que no admin apareça o campo personalizado filmes
campos = list(UserAdmin.fieldsets)
campos.append(
    ("Histórico", {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)

