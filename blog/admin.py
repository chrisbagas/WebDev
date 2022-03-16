from django.contrib import admin
from .models import Blog, Comments

admin.site.register(Comments)

admin.site.register(Blog)
# Register your models here.
