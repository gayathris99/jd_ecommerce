from django.urls import path 
from .views import *

app_name = "core"
urlpatterns = [
    path('', HomeView.as_view() , name = "homepage"),
    path('checkout/' , checkout , name = "checkout"),
    path('remove_from_cart/<slug>/', remove_from_cart , name = "remove_from_cart"),
    path('add_to_cart/<slug>/', add_to_cart , name = "add_to_cart"),
    path('products/<slug>/' ,ItemDetailView.as_view() , name = "products")
]