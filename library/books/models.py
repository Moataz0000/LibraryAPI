from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# when create user create token for him.
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings # to get defult user model


# Category --- Book


class Categorie(models.Model):
    name = models.CharField(max_length=200)
    ceartion_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    category = models.ForeignKey(Categorie, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    stock = models.IntegerField()
    ceartion_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)


    class Meta:
        ordering = ['-ceartion_date']


    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)    
    

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title  = models.CharField(max_length=100)
    body   = models.TextField()


    

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def TokenCreate(sender, instance, created,**kwargs):
    if created:
        Token.objects.create(user=instance)


















