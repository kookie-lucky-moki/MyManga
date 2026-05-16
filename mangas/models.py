from django.db import models
from django.urls import reverse
# Create your models here.

# Model of the categories of mnagas.
class Category(models.Model):
    title = models.CharField(max_length=250)

    class Meta:
        ordering = ('title',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title

# Model to create/publicate Mangas in the admin site.
class Manga(models.Model):
    category = models.ManyToManyField(Category, related_name='mangas')

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

# Model to add Chapters in the mangas
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
        return f'{self.manga.title} - Chapter {self.number}'

# Model to show the pages of the mangas
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
        return f'Page {self.page_number}'