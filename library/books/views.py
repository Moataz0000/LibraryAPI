from django.shortcuts import render, get_object_or_404
from .models import Book, Categorie, Post
from rest_framework.decorators import api_view
from .serializers import BookSerializer, CategoriesSerializer, Postserializer
from rest_framework import status, filters
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework import generics , mixins
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly

# without RESTframework -- FBV
def date_wihtout_REST(requset):
    books = [
        {
            'id':1,
            'title':'djanogforall',
            'slug':'djanogforall',
            'gategory':'programming',
            'price':'75$',
            'author':'Moataz Fawzy',
            'stock':100,
            'creation_date':'1/1/2024'
        },
        {
            'id':2,
            'title':'restframework',
            'slug':'restframework',
            'gategory':'programming',
            'price':'60$',
            'author':'Moataz Fawzy',
            'stock':70,
            'creation_date':'1/12/2024'
        }
    ]
    return JsonResponse(books, safe=False) # safe because the our date not hashbols.




# No REST from model
def no_rest_from_model(request):
    queryset = Book.objects.all().filter(active=True)
    
    response = {
        'queryset':list(queryset.values()) # in values you can add fields. and as default all fields will display

    }

    return JsonResponse(response)




# List == GET || Create == POST || Update == PUT || Delete == DELETE

# Function Based views [GET , POST ]
@api_view(['GET', 'POST'])
def FBV_list(request):
    
    # GET
    if request.method == 'GET':
        queryset = Book.objects.all().filter(active=True)
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data)

    # POST
    elif request.method == 'POST':
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.data , status=status.HTTP_400_BAD_REQUEST) # if serialize is not valid
        




# Function Based views [GET , PUT , DELETE ]
@api_view(['GET' , 'PUT' , 'DELETE'])
def FBV_with_PK(request, pk):
    try:
       queryset = get_object_or_404(Book, active=True , id=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   

    # GET
    if request.method == 'GET':
        serializer = BookSerializer(queryset)
        return Response(serializer.data)

    # PUT
    elif request.method == 'PUT':
        serializer = BookSerializer(queryset, data= request.data) # data with queryset i want to update.
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE
    elif request.method == 'DELETE':
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 

@api_view(['GET'])
def get_book_with_pk(requset, pk):
    queryset = get_object_or_404(Book, active=True, id=pk)
    serializer = BookSerializer(queryset) 
    return Response(serializer.data)



@api_view(['PUT'])
def update_book(request, pk):
    book = get_object_or_404(Book, active=True, id=pk)
    serializer = BookSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
def delete_book(request, pk):
    queryset = get_object_or_404(Book , active=True, id=pk)
    queryset.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)




# CBV - Class based views - List and create | GET , POST 
class CBV_List(APIView):

    def get(self, request):
        queryset = Book.objects.all().filter(active = True)
        serializer = BookSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, requset):
        serializer = BookSerializer(data=requset.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)     
    




# CBV | GET , PUT , DELETE --> wiht pk
class CBV_pk(APIView):

    def get(self, request, pk):
        queryset = get_object_or_404(Book, id=pk, active=True)
        serializer = BookSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        queryset = get_object_or_404(Book, active=True, id=pk)
        serializer = BookSerializer(queryset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        queryset = get_object_or_404(Book, id=pk, active=True)
        queryset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





# Mixins
class Mixins_List(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Book.objects.all().filter(active=True)
    serializer_class = BookSerializer


    def get(self, requset):
        return self.list(requset)
    
    def post(self, request):
        return self.create(request)
    


# Mixins | GET , PUT , DELETE ---- Retrieve , Update , Destroy by PK
class Mixins_Pk(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Book.objects.all().filter(active=True)
    serializer_class = BookSerializer

    def get(self, requset, pk):
        return self.retrieve(requset)
    
    def post(self, request, pk):
        return self.update(request)
    
    def delete(self, request, pk):
        return self.destroy(request)
    



# Generics | GET , POST 
class Generics_List(generics.ListCreateAPIView):
    queryset = Book.objects.all().filter(active=True)
    serializer_class = BookSerializer

    # Authentication this endpoint only.
    authentication_classes = [TokenAuthentication] 
    # permission_classes = [IsAuthenticated]




# Generics | GET , PUT , DELETE
class Generics_by_PK(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all().filter(active=True)
    serializer_class = BookSerializer

    # Authentication this class only.
    authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]





# Viewsets | GET , POST , PUT , DELETE
class Viewsets_books(viewsets.ModelViewSet):
    queryset = Book.objects.all().filter(active=True)
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'title']
    authentication_classes = [TokenAuthentication]



class Viewsets_Category(viewsets.ModelViewSet):
    queryset = Categorie.objects.all()
    serializer_class = CategoriesSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['id', 'name']



# search about book
@api_view(['GET'])  
def search_book(request): 
    queryset = Book.objects.filter(active=True, title = request.data['title'],id = request.data['id'])  
    serializer = BookSerializer(queryset, many=True)
    return Response(serializer.data)


# # Create a book
# @api_view(['POST'])
# def new_book(request):
#     category = get_object_or_404(Categorie,name=request.data['category'])
#     book = Book()
#     book.title = request.data['title']
#     book.slug  = request.data['slug']
#     book.category = category
#     # book.author = request.user
#     book.price = request.data['price']
#     book.stock = request.data['stock']
#     book.save()

#     return Response(status=status.HTTP_201_CREATED)



# post author editor
class Post_pk(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthorOrReadOnly]
    queryset = Post.objects.all()
    serializer_class = Postserializer