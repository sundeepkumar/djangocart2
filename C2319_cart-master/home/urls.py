from django.contrib import admin
from django.urls import path, include
from . import views
from .views import (remove_from_cart,
             add_to_cart,ProductView, HomeView,OrderSummaryView,reduce_quantity_item, ProductsView
                    )
#app_name="home"
urlpatterns = [
    path('', views.home, name='home'),
    #path('', HomeView.as_view(), name='home'),
    path('products/',ProductsView.as_view(), name='products'),
    path('product/<pk>/',ProductView.as_view(), name='product'),
    path('add-to-cart/<pk>/',add_to_cart,name='add-to-cart'),
    path('remove-from-cart/<pk>/',remove_from_cart, name='remove-from-cart'),
    path('order-summary', OrderSummaryView.as_view(), name='order-summary'),
    path('about/', views.about, name='about'),
    path('milestone_17/', views.milestone_17, name='milestone_17'),
    path('reduce-quantity-item/<pk>/', reduce_quantity_item, name='reduce-quantity-item')

]
