from django.shortcuts import render
from django.template import loader
from .models import Produit,Fournisseur
from django.http import request
from .forms import ProduitForm,FournisseurForm,UserRegistrationForm,UserCreationForm
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from magasin.models import Categorie,Produit
from magasin.serializers import CategorySerializer,ProduitSerializer
# Create your views here.
def index(request):
    if request.method == "POST" : 
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/magasin')
    else :
        form = ProduitForm() #créer formulaire vide
        list=Produit.objects.all()
    return render(request,'magasin/majProduits.html',{'form':form ,'list':list})
def nouveauFournisseur(request):
    if request.method == "POST" :
        form = FournisseurForm(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            nouvFournisseur=Fournisseur.objects.all()
        return render(request,'magasin/vitrineF.html',{'nouvFournisseur':nouvFournisseur})
    else : 
        form = FournisseurForm() #créer formulaire vide 
        nouvFournisseur=Fournisseur.objects.all()
    return render(request,'magasin/fournisseur.html',{'form':form,'nouvFournisseur':nouvFournisseur})


@login_required
def home(request):
    return render(request,'magasin/accueil.html')

def register(request):
  if request.method == 'POST' :
      form = UserCreationForm(request.POST)
      if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           password = form.cleaned_data.get('password1')
           user = authenticate(username=username, password1=password)
           login(request,user)
           messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
      return redirect('home')
  else :
        form = UserCreationForm()
  return render(request,'registration/register.html',{'form' : form})

class CategoryAPIView(APIView):
    def get(self, *args, **kwargs):
        categories = Categorie.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

   
class ProduitAPIView(APIView):
   def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)
class ProduitAPIView(APIView):
   def get(self, *args, **kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)


                



    