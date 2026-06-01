import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser

# Modelo para las categorías de mangas
class Category(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categorías'

    def __str__(self):
        return self.title

# Modelo para crear/publicar mangas en el panel de administración
class Manga(models.Model):
    category = models.ManyToManyField(
        Category,
        related_name='mangas'
    )

    title = models.CharField(max_length=250)
    author = models.CharField(max_length=250)

    description = models.TextField()

    cover = models.ImageField(upload_to='covers/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('manga_detail', args=[self.slug])


# Modelo para agregar capítulos a los mangas
class Chapter(models.Model):
    manga = models.ForeignKey(
        Manga,
        related_name='chapters',
        on_delete=models.CASCADE
    )

    title = models.CharField(max_length=250)
    number = models.DecimalField(max_digits=5, decimal_places=1)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.manga.title} - Capítulo {self.number}'


# Modelo para mostrar las páginas de los mangas
class Page(models.Model):
    chapter = models.ForeignKey(
        Chapter,
        related_name='pages',
        on_delete=models.CASCADE
    )

    image = models.ImageField(upload_to='pages/')

    page_number = models.PositiveIntegerField()

    class Meta:
        ordering = ['page_number']

    def __str__(self):
        return f'Página {self.page_number}'
    
# Modelo para los usuarios registrados
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    is_seller = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='mangas_user_set',
        blank=True,
        help_text='The groups this user belong to.',
        verbose_name='groups',
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='mangas_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    def __str__(self):
        return self.username