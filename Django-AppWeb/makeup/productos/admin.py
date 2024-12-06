from django.contrib import admin
from .models import Post
from django.contrib import admin
from .models import Product, usuario

admin.site.register(Post)
admin.site.register(Product)
admin.site.register(usuario)

# Register your models here.
