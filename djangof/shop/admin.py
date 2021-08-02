from django.contrib import admin
from .models import Cart, Product, CartProduct, Category, Order, Favourite


admin.site.register([Cart, Product, CartProduct, Category, Order, Favourite, ])
