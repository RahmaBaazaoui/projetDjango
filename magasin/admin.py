from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Produit)
admin.site.register(Fournisseur)
admin.site.register(Categorie)
admin.site.register(Commande)
admin.site.register(ProduitC)
admin.site.register(ProduitNC)
