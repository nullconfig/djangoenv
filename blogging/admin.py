from django.contrib import admin
from blogging.models import Post, Category

class InLineCategory(admin.TabularInline):
    model = Category.posts.through
    extra = 1
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [InLineCategory]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)
