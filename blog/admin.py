from django.contrib import admin

# Register your models here.
from blog.models import Tag, Post, PostAdmin

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)

