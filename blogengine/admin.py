from django.contrib import admin
from django.contrib.auth.models import User

from .models import Post, Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


class CategoryToPostInline(admin.TabularInline):
    model = Category.CategoryToPost
    extra = 1


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    exclude = ('author',)
    inlines = [CategoryToPostInline]

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        obj.save()


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
