from django.db import models


class Categories(models.Model):
    nom = models.CharField(max_length=100, unique=True)
    def __str__(self):
        return self.nom        

class Articles(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.FloatField()
    stock = models.IntegerField()
    categorie_id = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name="articles")
    

    def __str__(self):
        return self.nom

    def decrease_stock(self, quantity):
        if self.stock <= 0: 
           return False
        else :    
           self.stock -= quantity
           self.save()
           return self.stock
        
