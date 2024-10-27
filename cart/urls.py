from django.urls import path
from .views import UserFacturesView, FactureDetailView, SubmitCartView, CartDoneView, CartView

app_name = 'cart'

urlpatterns = [
    path('factures/', UserFacturesView.as_view(), name='user_factures'),
    path('factures/<int:facture_id>/', FactureDetailView.as_view(), name='facture_detail'),
    path('submit-cart/', SubmitCartView.as_view(), name='submit_cart'),
    path('done', CartDoneView.as_view(), name='cart_done'),
    path('', CartView.as_view(), name='cart_view'),
]
