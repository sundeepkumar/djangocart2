from django.contrib import admin
from .models import Post
#from home.models import Item, OrderItem, Order

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'body', 'publish')
    # prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
#admin.site.register(Item)
#admin.site.register(OrderItem)
#admin.site.register(Order)
