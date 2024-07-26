from rest_framework import serializers
from .models import Categorie , Book , Post




class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'




class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'



class Postserializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    