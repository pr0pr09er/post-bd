from django.contrib import admin
from .models import Post, Category, Publisher, Author

# Register your models here.
admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Author)