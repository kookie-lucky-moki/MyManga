from django.shortcuts import render, get_object_or_404

from .models import Manga, Chapter

def home(request):
    mangas = Manga.objects.all()

    return render(request, 'mangas/home.html', {
        'mangas': mangas
    })


def login_view(request):
    return render(request, 'mangas/login.html')


def search(request):
    query = request.GET.get('q')

    mangas = Manga.objects.filter(
        title__icontains=query
    ) if query else []

    return render(request, 'mangas/search.html', {
        'mangas': mangas,
        'query': query
    })


def manga_detail(request, slug):
    manga = get_object_or_404(
        Manga,
        slug=slug
    )

    return render(request, 'mangas/manga_detail.html', {
        'manga': manga
    })

def reader(request, slug, chapter_id):
    manga = get_object_or_404(
        Manga,
        slug=slug
    )

    chapter = get_object_or_404(
        Chapter,
        id=chapter_id,
        manga=manga
    )

    return render(request, 'mangas/reader.html', {
        'manga': manga,
        'chapter': chapter
    })