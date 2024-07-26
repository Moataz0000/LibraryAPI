from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('books.urls')),
    path('api-auth/', include('rest_framework.urls')),  # Ensure you use a trailing slash here

]
