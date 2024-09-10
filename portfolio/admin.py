from django.contrib import admin
from .models import Home, Profile, Category, Skills, Portfolio, About, Message


# Home
admin.site.register(Home)


# About
class ProfileInline(admin.TabularInline):
    model = Profile
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInline,
    ]

# Skills
class SklillsInline(admin.TabularInline):
    model = Skills
    extra = 2

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = [
        SklillsInline,
    ]


# Portfolio
admin.site.register(Portfolio)


# Message
admin.site.register(Message)