from django.db import models
from django.utils.text import slugify

# Create your models here.
import hashlib
from tinymce.models import HTMLField

from django.contrib.auth.models import User

# User

from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


########################################## U T I L I S A T E U R ###########################################

class Utilisateur(models.Model):
    """Model definition for Utilisateur."""

    # TODO: Define fields here
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='utilisateur')
    photo = models.ImageField(upload_to='photo_utilisateur', default="profileimage.png", null = True, blank = True)
    lieu_habitat = models.CharField(max_length=255, null = True, blank = True)
    genre = models.CharField(max_length=50,null = True, blank = True)
    date_naissance = models.DateField(blank = True, null = True)


    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    class Meta:
        """Meta definition for Utilisateur."""

        verbose_name = 'Utilisateur'
        verbose_name_plural = 'Utilisateurs'

    def __str__(self):
        """Unicode representation of Utilisateur."""
        return self.user.username

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Utilisateur.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
            
        instance.utilisateur.save()




########################################## CATEGORIE ARTICLE ###########################################
class Categorie(models.Model):
    """Model definition for Categorie."""

    # TODO: Define fields here
    nom = models.CharField(unique=True,max_length=255)
    titre_slug = models.SlugField(editable=False, null=True, max_length=255)
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        encoded_id = hashlib.md5(str(self.id).encode())
        self.titre_slug = slugify(self.nom+' '+str(encoded_id.hexdigest()))
        super(Categorie, self).save(*args, **kwargs)
        

    class Meta:
        """Meta definition for Categorie."""

        verbose_name = 'Categorie'
        verbose_name_plural = 'Categories'

    def __str__(self):
        """Unicode representation of Categorie."""
        return self.nom


########################################## ARTICLE ###########################################

class Article(models.Model):
    """Model definition for Article."""

    # TODO: Define fields here
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article_auteur',blank=True, null=True)
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE, related_name="categoriearticle",)
    titre = models.CharField(max_length=255,)
    titre_slug = models.SlugField(unique=True, editable=False, null=True, blank=True, max_length=255)
    image = models.ImageField(upload_to="imagearticle")
    description  = HTMLField('description')
    viewed = models.BooleanField(default=False)
    statut = models.BooleanField(default=False)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        encoded_id = hashlib.md5(str(self.id).encode())
        self.titre_slug = slugify(self.titre+' '+str(encoded_id.hexdigest()))
        super(Article, self).save(*args, **kwargs)

    class Meta:
        """Meta definition for Article."""
        ordering = ['-date_add']
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'
    
    def __str__(self):
        """Unicode representation of Article."""
        return self.titre
    
    def get_absolute_url(self):
        return f'/detail/{self.titre_slug}'
    



########################################## COMMENTAIRE ARTICLE ###########################################

class Commentaire(models.Model):
    """Model definition for Commentaire."""

    # TODO: Define fields here
    auteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='usercommentaire', blank=True, null = True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name="commentairearticle", null=True)
    email = models.EmailField(max_length=255)
    message = models.TextField(null=True)
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True, null=True)
    date_upd = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        """Meta definition for Commentaire."""

        verbose_name = 'Commentaire'
        verbose_name_plural = 'Commentaires'

    def __str__(self):
        """Unicode representation of Commentaire."""
        return self.email


