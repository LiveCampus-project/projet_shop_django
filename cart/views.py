from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.utils import timezone
from .models import Facture, User, Facture_Articles
from .forms import CartForm  # You may want to create a form for submitting a cart

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
        # This view handles submitting the cart and creating a new facture
        # Assuming you have a CartForm that gathers necessary information
        form = CartForm(request.POST)

        if form.is_valid():
            # Create the new Facture
            facture = Facture(
                date_emission=timezone.now(),
                id_delivery=form.cleaned_data['delivery'],
                total_htc=0,  # Will calculate later
                client_id=request.user
            )
            facture.save()

            # Add articles from the cart to the Facture_Articles
            articles = form.cleaned_data['articles']  # Assuming this is a list of articles with quantity
            total = 0
            for article in articles:
                quantity = article['quantity']
                facture_article = Facture_Articles(
                    facture_id=facture,
                    article_id=article['article'],  # Assuming this is the article instance
                    quantity=quantity
                )
                facture_article.save()
                total += article['article'].prix * quantity  # Calculate total

            # Update total in the facture
            facture.total_htc = total + facture.id_delivery.prix  # Adding delivery price
            facture.save()

            return redirect('cart:user_factures')  # Redirect to the factures list after submission

        return render(request, 'cart/cart.html', {'form': form})  # Render the cart form again if invalid
