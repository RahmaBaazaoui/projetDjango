from django.db import models
from datetime import date
# Create your models here.
class Categorie(models.Model):
    name= models.CharField(max_length=50)
    def __str__(self):
        return str(self.id)+self.name  
    
class Produit(models.Model):
    TYPE_CHOICES=[('fr','Frais'),('cs','Conserve'),('em','emballé')]
    libelle=models.CharField(max_length=255)
    description=models.TextField()
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0.000)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    categorie= models.ForeignKey('Categorie',on_delete=models.CASCADE,default=1 )
    img=models.ImageField(blank=True) #default='aliment.jpg'
    fournisseur=models.ForeignKey('Fournisseur', on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.libelle+" "+self.description+" "+str(self.prix)
class Fournisseur(models.Model):
    nom=models.CharField(max_length=255)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)
    
    def __str__(self):
        return self.nom+" "+self.adresse

class Commande(models.Model):
    dateCde=models.DateField(null=True, default=date.today)
    produits=models.ManyToManyField('Produit')
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    
    def __int__(self):
        return self.dateCde+""+self.totalCde
    
class ProduitC(Produit):
    duree_garantie=models.IntegerField()
    def __str__(self):
        return "Produit consommable, garantie : "+str(self.duree_garantie)

class ProduitNC(Produit):
        duree_garantie = models.CharField(max_length=100)

        def __str__(self):
            return f"({self.libelle} ({self.description}) - {self.prix} dt - {self.type} - {self.duree_garantie})"
