from email import message
from rest_framework import generics 
from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import (AllowAny,  
                                        IsAuthenticated,
                                        IsAuthenticatedOrReadOnly,
                                        IsAdminUser,
                                        SAFE_METHODS
                                        )

from .models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer, ProductoCreateSerializer


#Lista de productos
class ProductosApiView(ListAPIView):
    serializer_class = ProductoSerializer

    def get_queryset(self):
        return Producto.objects.all()
    


# Lista y creación de productos por admin 
class ProductoCreateApiView(CreateAPIView):
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def post(self, request: Request):
        serializer = self.serializer_class(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response ({ 'message': "Producto creado correctamente"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Detalle de cada producto
class ProductoRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(id = self.kwargs['pk'])


    

#Editar producto 
class ProductoUpdateApiView(generics.RetrieveUpdateAPIView):

    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer



#Eliminar producto 
class ProductoDestroyApiView(generics.DestroyAPIView):
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(id = self.kwargs['pk'])





# Lista de categorias
class CategoriaApiView(ListAPIView):
    serializer_class = CategoriaSerializer
    

    def get_queryset(self):
        return Categoria.objects.all()


