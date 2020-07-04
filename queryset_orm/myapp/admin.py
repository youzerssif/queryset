from django.contrib import admin

# Register your models here.
# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class UtilisateurAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'photo',
        'lieu_habitat',
        'genre',
        'date_naissance',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'user',
        'date_naissance',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'user',
        'photo',
        'lieu_habitat',
        'genre',
        'date_naissance',
        'statut',
        'date_add',
        'date_upd',
    )


class CategorieAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'titre_slug',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'titre_slug',
        'statut',
        'date_add',
        'date_upd',
    )


class ArticleAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'auteur',
        'categorie',
        'titre',
        'titre_slug',
        'image',
        'description',
        'viewed',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'auteur',
        'categorie',
        'viewed',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'auteur',
        'categorie',
        'titre',
        'titre_slug',
        'image',
        'description',
        'viewed',
        'statut',
        'date_add',
        'date_upd',
    )


class CommentaireAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'auteur',
        'article',
        'email',
        'message',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'auteur',
        'article',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'auteur',
        'article',
        'email',
        'message',
        'statut',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Utilisateur, UtilisateurAdmin)
_register(models.Categorie, CategorieAdmin)
_register(models.Article, ArticleAdmin)
_register(models.Commentaire, CommentaireAdmin)
