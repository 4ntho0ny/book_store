from django.contrib import admin
from .models import Book, Author, Address

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    # prepopulated_fields = {"slug": ("title",)} # don't work with readonly_fields
    list_filter = ("author", "rating")
    list_display = ("title", "author")
    
admin.site.register(Book, BookAdmin)
admin.site.register(Author)
admin.site.register(Address)