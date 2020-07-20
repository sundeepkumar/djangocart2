from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse
from .models import About
from django.contrib import messages
from django.views.generic import ListView, DetailView,  View
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import (
Item, Order, OrderItem
)
# Create your views here.
def home(request):
    return render(request, '../templates/home.html', {'title': 'Home'})

def about(request):
    return render(request, '../templates/about.html', {'title': 'About'})

def milestone_17(request):
    return render(request, '../templates/milestone_17.html', {'title': 'Milestone 17'})

def forsale(request):
    return render(request, '../templates/forsale.html', {'title': 'For Sale'})

class HomeView(ListView):
    model= Item
    template_name = "home.html"

class ProductsView(ListView):
    model= Item
    template_name = "products.html"

class ProductView(DetailView):
    model = Item
    template_name = "product.html"

class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):

        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            context = {
                'object' : order
            }
            return render(self.request, 'order_summary.html', context)
        except ObjectDoesNotExist:
            messages.error(self.request, "You do not have an order")
            return redirect("/")

def add_to_cart(request, pk):
    item = get_object_or_404(Item,pk = pk)
    order_item,created= OrderItem.objects.get_or_create(item= item, user=request.user, ordered = False)
    order_qs = Order.objects.filter(user = request.user, ordered = False)
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "Added Quantity Item!")
            return redirect("product", pk = pk)
        else:
            order.items.add(order_item)
            messages.info(request,"ITem added to your cart")
            return redirect("product",pk=pk)
    else:
        ordered_date=timezone.now()
        order=Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request,"items added to your cart")
        return redirect("product",pk=pk)
    ordered_date=timezone.now()
    order=Order.objects.create(user=request.user)
    order.items.add(order_item)
    messages.info(request,"items added to your cart")
    return redirect("product",pk=pk)

def remove_from_cart(request,pk):
    item = get_object_or_404(Item, px=pk)
    order_qs=Order.objects.filter(user=request.user,ordered=False)
    if order_qs.exists():
        order=order_qs[0]
        if order.items.filter(item__pk= item.pk).exists():
            order_item=OrderItem.objects.filter(item=item,user=request.user,ordered=False)[0]
            order_item.delete()
            messages.info(request,"Item \""+ order_item.item.item_name+"\"removed from your cart")
            return redirect("product")
        else:
            messages.info(request,"this item not in your cart")
            return redirect("product",pk=pk)
    else:
        messages.info(request,"you do not have an order")
        return redirect("product",pk=pk)

def reduce_quantity_item(request, pk):
    item = get_object_or_404(Item, pk=pk )
    order_qs = Order.objects.filter(
        user = request.user, 
        ordered = False
    )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__pk=item.pk).exists() :
            order_item = OrderItem.objects.filter(
                item = item,
                user = request.user,
                ordered = False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order_item.delete()
            messages.info(request, "Item quantity was updated")
            return redirect("order-summary")
        else:
            messages.info(request, "This Item not in your cart")
            return redirect("order-summary")
    else:
        #add message doesnt have order
        messages.info(request, "You do not have an Order")
        return redirect("order-summary")

