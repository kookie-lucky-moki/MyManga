from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Category, Manga, Chapter, Page, User

# USER
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_seller', 'is_staff')
    list_filter = ('is_seller',)

    fieldsets = BaseUserAdmin.fieldsets + (
        ('Roles de Usuario', {'fields': ('is_seller',)}),
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        ('Roles de Usuario', {'fields': ('is_seller',)}),
    )

# CATEGORY
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)


# PAGE INLINE
class PageInline(admin.TabularInline):
    model = Page
    extra = 1


# CHAPTER ADMIN
@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'manga',
        'number',
        'title',
        'created_at'
    )

    list_filter = ('manga',)
    search_fields = ('title',)

    inlines = [PageInline]


# MANGA ADMIN
@admin.register(Manga)
class MangaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'title',
        'author',
        'created_at'
    )

    prepopulated_fields = {
        'slug': ('title',)
    }

    search_fields = (
        'title',
        'author'
    )

    list_filter = (
        'category',
        'created_at'
    )

    filter_horizontal = ('category',)


# PAGE ADMIN
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'chapter',
        'page_number'
    )

    list_filter = ('chapter',)