from django.shortcuts import render, redirect, get_object_or_404
from .models import Item , OrderItem , Order
from django.views.generic import ListView , DetailView
from django.utils import timezone
from django.contrib import messages
app_name = "core"

def checkout(request):
    return render(request , "checkout-page.html")
     
class HomeView(ListView):
    model = Item
    template_name = 'home-page.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'product-page.html'


def add_to_cart(request,slug):
    item = get_object_or_404(Item, slug=slug)
    order_item , created = OrderItem.objects.get_or_create(
        item=item,
        user = request.user,
        ordered = False

        )
    order_qs = Order.objects.filter(user = request.user ,ordered = False)

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Item Updated")
        else:
            messages.info(request, "Item Added")
            order.items.add(order_item)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user , ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "Item Added")
    return redirect('core:products',slug=slug)



def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
    )
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=request.user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request, "This item was removed from your cart.")
            return redirect("core:products" , slug=slug)
        else:
            messages.info(request, "This item was not in your cart")
            return redirect("core:products", slug=slug)
    else:
        messages.info(request, "You do not have an active order")
        return redirect("core:products", slug=slug)

















