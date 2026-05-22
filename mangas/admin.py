from django.contrib import admin

from .models import Category, Manga, Chapter, Page


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