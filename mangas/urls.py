from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('login/', views.login_view, name='login'),

    path('search/', views.search, name='search'),

    path('manga/<slug:slug>/', views.manga_detail, name='manga_detail'),

    path('reader/<int:chapter_id>/', views.reader, name='reader'),
]