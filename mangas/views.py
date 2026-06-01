from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from .models import Manga, Chapter

def home(request):
    mangas = Manga.objects.all()

    return render(request, 'mangas/home.html', {
        'mangas': mangas
    })


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()

    return render(request, 'mangas/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect('home')

    return render(request, 'mangas/login.html')


def logout_view(request):
    logout(request)
    return redirect('home')


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