from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
CATEGORY = (
    (0,"Electronic"),
    (1,"Furniture"),
    (2,"Major Appliance"),
    (3,"Kitchen"),
    (4,"Books"),
    (5,"Motors"),
    (6,"Music"),
    (7,"Other")
)
LABEL = (
    (0,"Best-Seller"),
    (1, "Must Have"),
    (2,"durable"),
    (3,"Best Bang for your buck"),
    (4,"Pollitzer Award")
)
CONDITION = {
    (0,"Brand New"),
    (1, "Used - Like New"),
    (2, "Used - Good"),
    (3, "Used - Poor Condidtion"),
    (4, "Used - Not Usable")
}

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post" , null=True)
    title = models.CharField(max_length=50)
    body = models.TextField(null=True, max_length=300)
    updated_on = models.DateTimeField(auto_now= True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    category = models.IntegerField(choices=CATEGORY, default=0)
    cover = models.ImageField(upload_to='images/', null=True , blank=True)
    condition = models.IntegerField(choices=CONDITION , default = 4)
    price = models.DecimalField(max_digits=11 , decimal_places=2, default=Decimal(0.00), null=True ,blank=True, validators=[MinValueValidator(0.00) , MaxValueValidator(9999999999)])
    publish = models.IntegerField(choices=STATUS, default=0)
  
    

