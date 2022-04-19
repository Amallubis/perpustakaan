from tkinter import W
from django.urls import path
from perpustakaan import views

app_name = 'perpustakaan'
urlpatterns = [ 
    path('tambah-buku/', views.tambah_buku, name='tambahbuku'),
]