from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.utils import timezone
from .models import Facture, User, Facture_Articles, Delivery  # Import your models
from shop.models import Articles  # Import your models
from .forms import CartForm  # You may want to create a form for submitting a cart
import json



class CartView(View):
    def get(self, request):
        return render(request, 'cart/cart.html', {'form': CartForm()})

class UserFacturesView(View):
    def get(self, request):
        # Retrieve all factures for the logged-in user
        factures = Facture.objects.filter(client_id=request.user)
        return render(request, 'cart/user_factures.html', {'factures': factures})


class FactureDetailView(View):
    def get(self, request, facture_id):
        # Retrieve a specific facture
        facture = get_object_or_404(Facture, id=facture_id, client_id=request.user)
        return render(request, 'cart/facture_detail.html', {'facture': facture})


class SubmitCartView(View):
    def post(self, request):
        print('POST request received')

        # Parse the articles from the request
        articles = json.loads(request.POST.get('articles', '[]'))  # Load the articles from JSON

        # Validate and process the data
        delivery = Delivery.objects.get(id=1)  # get first delivery

        if articles:  # Proceed only if articles are available
            # Create the new Facture (make sure to adjust based on your form requirements)
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
                # Assuming you have a method to retrieve the article by ID
                article_instance = Articles.objects.get(id=article['article'])  # Adjust based on your model
                facture_article = Facture_Articles(
                    facture_id=facture,
                    article_id=article_instance,  # Assuming this is the article instance
                    quantity=quantity
                )
                facture_article.save()
                total += article_instance.prix * quantity  # Calculate total

            # Update total in the facture
            facture.total_htc = total  # Adjust based on your pricing logic
            facture.save()

            return redirect('cart:user_factures')  # Redirect to the factures list after submission

        return render(request, 'cart/cart.html', {'form': CartForm()})  # Render the cart form again if invalid

    def get(self, request):
        return render(request, 'cart/cart.html', {'form': CartForm()})

class CartDoneView(View):
    def get(self, request):
        return render(request, 'cart/cart_done.html')