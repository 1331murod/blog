from django.contrib import admin
from .models import ProfileData, SocialLink, Service, About, Tools, Post, Project, Tag, Category, PostCategory


@admin.register(ProfileData)
class Profiledata(admin.ModelAdmin):
    list_display = ('id', 'full_name')
    list_display_links = ('id', 'full_name')
    search_fields = ('full_name', )
    list_filter = ('full_name', )


@admin.register(SocialLink)
class SocialLink(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'url', 'order')
    list_display_links = ('id', 'name', 'icon')
    search_fields = ('name', 'icon', )
    list_filter = ('name', 'icon', )
    



@admin.register(Service)
class Service(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon')
    list_display_links = ('id', 'name', 'icon')
    search_fields = ('name', 'icon', )
    list_filter = ('name', 'icon', )
    


@admin.register(About)
class About(admin.ModelAdmin):
    list_display = ('id', 'projects', 'money', 'valentures')
    list_display_links = ('id', 'projects', 'money')
    search_fields = ('money', 'valentures', )
    list_filter = ('money', 'projects', )


@admin.register(Tools)
class Tools(admin.ModelAdmin):
    list_display = ('id', 'title', 'percentage', 'order')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'order', )
    list_filter = ('title', 'percentage', )


@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'creat_at')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'Tag', 'category', )
    list_filter = ('name',
                    'creat_at', )

@admin.register(Project)
class Project(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_filter = ('name', 'category',  )

@admin.register(Tag)
class Tag(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name', )
    list_filter = ('name', )

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links =  ('id', 'name')
    search_fields = ('name', )
    list_filter = ('name', )

@admin.register(PostCategory)
class Postcategpry(admin.ModelAdmin):
    list_display  = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('id', 'name', )
    list_filter = ('name', )
