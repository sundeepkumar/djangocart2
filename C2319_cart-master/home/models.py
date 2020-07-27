from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from posts.models import CATEGORY
from posts.models import LABEL
from posts.models import CONDITION
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from posts.models import Post
from django.contrib.auth.models import User

# Create your models here.

class About(models.Model):
    about_title = models.CharField(max_length=200)
    about_content = models.TextField()

    def __str__(self):
        return self.about_title


class Item(models.Model):
    #item_name = models.CharField(max_length=100)
    #price = models.FloatField()
    #category = models.IntegerField(choices=CATEGORY, default=0)
    #item_label = models.CharField(choices=LABEL, default=0, max_length =100)
    #condition = models.IntegerField(choices=CONDITION , default = 4)
    #decsription = models.TextField()
    item_name = models.CharField(max_length=100)	
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="item" , null=True)
    #title = models.CharField(max_length=50)
    body = models.TextField(null=True, max_length=300)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    category = models.IntegerField(choices=CATEGORY, default=0)
    cover = models.ImageField(upload_to='images/', null=True , blank=True)
    #item_label = models.CharField(choices=LABEL, default=0,max_length =100)
    condition = models.IntegerField(choices=CONDITION , default = 4)
    price = models.DecimalField(max_digits=11 , decimal_places=2, default=Decimal(0.00), null=True ,blank=True, validators=[MinValueValidator(0.00) , MaxValueValidator(9999999999)])
    #publish = models.IntegerField(choices=STATUS, default=0)
    description = models.TextField(null=True, max_length=300)
    post = models.ForeignKey(Post, on_delete = models.CASCADE,related_name="post" , null=True)
    imgurl  = models.TextField(default = "https://mdbootstrap.com/img/Photos/Horizontal/E-commerce/Vertical/12.jpg")
    discount_price = models.FloatField(blank=True, null=True)
    

    


    def __str__(self):
        return self.item_name

    def get_absolute_url(self):
        return reverse("product", kwargs={"pk": self.pk})  # see how it passes arguments

    def get_add_to_cart_url(self):
        return reverse("add-to-cart", kwargs={"pk": self.pk})


    def get_remove_from_cart_url(self):
        return reverse("remove-from-cart",kwargs={"pk": self.pk})

    def get_img_url(self):
        return self.imgurl

class OrderItem(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name="orderitem", null=True)
    ordered = models.BooleanField(default = False)
    item = models.ForeignKey(Item, on_delete = models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.item_name}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_discount_item_price()
        return self.get_total_item_price()

class Order(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name="order", null=True)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default = False)

    def __str__(self):
        return self.user.username

    def get_total_price(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
