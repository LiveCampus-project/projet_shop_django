from django.db import models
from account.models import User
from shop.models import Articles



class Delivery(models.Model):
    delivery_system = models.CharField(max_length=100)
    description = models.TextField()
    prix = models.FloatField()
    
    def __str__(self):
        return self.delivery_system
    

class Facture(models.Model):
    date_emission = models.DateField()
    id_delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name="factures")
    total_htc = models.FloatField()
    client_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="factures")
    
    
    def __str__(self):
        return f"Facture for {self.client_id.username} on {self.date_emission} - Total: {self.total_htc}"

    def get_total_htc(self):
        articles_price = Facture_Articles.objects.filter(facture_id=self.id)
        delivery_price = self.id_delivery.prix
        total = sum(article.article_id.prix * article.quantity for article in articles_price)
        total += delivery_price
        return total



class Facture_Articles(models.Model):
    facture_id = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name="articles")
    article_id = models.ForeignKey(Articles, on_delete=models.CASCADE, related_name="factures")
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"Facture {self.facture_id.id} - Article: {self.article_id.nom} (Quantity: {self.quantity})"




