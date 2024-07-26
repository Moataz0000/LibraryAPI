from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token




router = DefaultRouter()
router.register('books', views.Viewsets_books)
router.register('categories', views.Viewsets_Category)

urlpatterns = [ 

    # without RESTframework
    path('api-books/', views.date_wihtout_REST),
    path('api-books-model/', views.no_rest_from_model),

    # use Restframework - FBV || GET , POST
    path('rest/api-books/', views.FBV_list),
    path('api-book/<int:pk>/', views.FBV_with_PK),

    # get , delete , update
    path('get-api/<int:pk>/', views.get_book_with_pk),
    path('update-api/<int:pk>/', views.update_book),
    path('delete-api/<int:pk>/', views.delete_book),  

    # CBV | GET - POST | "APIViews"
    path('rest-cbv/', views.CBV_List.as_view()),
    path('rest-cbv/<int:pk>/', views.CBV_pk.as_view()),

    # Mixins | GET , POST , DELETE by pk
    path('rest-mixins/', views.Mixins_List.as_view()),
    path('rest-mixins/<int:pk>/', views.Mixins_Pk.as_view()),


    # Generics | GET , POST
    path('rest-generics/', views.Generics_List.as_view()),
    path('rest-generics/<int:pk>/', views.Generics_by_PK.as_view()),


    # Viewsets | GET , POST , PUT , DELETE
    path('rest/viewsets/',include(router.urls)),
    path('rest-viewset/', include(router.urls)),

    # search book
    path('fbv/find-book/', views.search_book),

    # new book
    # path('fbv-newbook/', views.new_book),

    

    # Token Auth
    path('api-token-auth', obtain_auth_token), # this url to know the client model token generate



    # Post Pk Generics
    path('post-generics/<int:pk>', views.Post_pk.as_view()),
]