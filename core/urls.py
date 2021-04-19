from django.urls import path 
from .views import *

urlpatterns = [
    path('', HomeView.as_view() , name = "homepage"),
    path('checkout/' , checkout , name = "checkout"),
    path('products/<slug>/' ,ItemDetailView.as_view() , name = "products")
]