from django.urls import path
from .views import CategoryAPIView,ProduitAPIView
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('nouvFournisseur/',views.nouveauFournisseur,name='nouvFournisseur'),
    path('liste/', views.index,name='index'),
    path('register/',views.register, name = 'register'),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/produits/', ProduitAPIView.as_view()),
]
