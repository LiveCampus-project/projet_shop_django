from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.utils import timezone
from .models import Facture, User, Facture_Articles, Delivery  
from shop.models import Articles  
from .forms import CartForm  
import json



class CartView(View):
    def get(self, request):
        return render(request, 'cart/cart.html', {'form': CartForm()})

class UserFacturesView(View):
    def get(self, request):
        factures = Facture.objects.filter(client_id=request.user).select_related('id_delivery')
        
        return render(request, 'cart/user_factures.html', {'factures': factures})


class FactureDetailView(View):
    def get(self, request, facture_id):
        facture = get_object_or_404(Facture, id=facture_id, client_id=request.user)
       
        facture_articles = Facture_Articles.objects.filter(facture_id=facture_id)

        return render(request, 'cart/facture_detail.html', {'facture': facture, 'facture_articles': facture_articles})


class SubmitCartView(View):
    def post(self, request):
        print('POST request received')

        articles = json.loads(request.POST.get('articles', '[]')) 

        delivery = Delivery.objects.get(id=1)  # get first delivery

        if articles:  
            facture = Facture(
                date_emission=timezone.now(),
                id_delivery=delivery,  # Correctly assign delivery to the id_delivery field
                total_htc=0,
                client_id=request.user
            )
            facture.save()

            total = 0
            for article in articles:
                quantity = article['quantity']
            
                article_instance = Articles.objects.get(id=article['id']) 
                facture_article = Facture_Articles(
                    facture_id=facture,
                    article_id=article_instance, 
                    quantity=quantity
                )
                facture_article.save()
                total += article_instance.prix * quantity  

            facture.total_htc = total  
            facture.save()

            return redirect('cart:user_factures')  

        return render(request, 'cart/cart.html', {'form': CartForm()}) 

    def get(self, request):
        return render(request, 'cart/cart.html', {'form': CartForm()})

class CartDoneView(View):
    def get(self, request):
        return render(request, 'cart/cart_done.html')