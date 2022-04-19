"""perpus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView,LogoutView
from perpustakaan import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('perpustakaan.urls', namespace='perpustakaan')),
    path('buku/',views.index, name='buku'),
    path('buku/ubah/<int:id_buku>', views.ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>',views.hapus_buku, name='hapus_buku'),
    path('masuk/',LoginView.as_view(), name='masuk'),
    path('keluar/',LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('signup', views.signup, name='signup'),
]
