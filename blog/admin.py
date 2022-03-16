from django.contrib import admin
from .models import Blog, Comments

admin.site.register(Comments)

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ['creator']

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        obj.last_modified_by = request.user
        obj.save()
admin.site.register(Blog, BlogAdmin)
# Register your models here.
