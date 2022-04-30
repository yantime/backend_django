from django.urls import path
from .views import ProductosApiView, ProductoCreateApiView, CategoriaApiView, ProductoRetrieveApiView,ProductoDestroyApiView, ProductoUpdateApiView   

urlpatterns = [
    path('', ProductosApiView.as_view()),
    path('<int:pk>/', ProductoRetrieveApiView.as_view()),
    path('create/', ProductoCreateApiView.as_view()),
    path('delete/<int:pk>/', ProductoDestroyApiView.as_view()),
    path('update/<int:pk>/', ProductoUpdateApiView.as_view()),
    path('categorias/', CategoriaApiView.as_view()),
    
]