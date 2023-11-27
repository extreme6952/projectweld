from django.contrib import admin

from .models import Comment, Product,Gallery




class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):

    list_display = ['title','slug','publish','status']

    list_filter = ['status','created','publish']

    search_fields = ['title','body']

    inlines = [GalleryInline,]

    prepopulated_fields = {'slug':('title',)}

    date_hierarchy = 'publish'

    ordering = ['status','publish']


@admin.register(Comment)

class CommentAdmin(admin.ModelAdmin):

    list_display = ['name','email','product','created','active']

    list_filter = ['active','created','updated']

    search_fields = ['body','name','email']


