from django.contrib import admin
from .models import *



admin.site.register(Categorie)

admin.site.register(Post)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    readonly_fields = ['slug']
    list_display = ['title', 'category', 'price', 'ceartion_date']