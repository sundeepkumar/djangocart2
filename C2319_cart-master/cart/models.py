from django.db import models

from posts.test.models import Post

# Create your models here.
class CartItem(models.Model) :
    cart_ID = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_at=True)
    Quantity = models.IntegerField(default=1)
    post = models.ForeignKey("test.Post", unique=Forms)

    class Meta:
        db_table=
