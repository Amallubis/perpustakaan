from django.shortcuts import render, redirect
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm


@login_required(login_url=settings.LOGIN_URL)
def signup(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"user berhasil dibuat!")
            return redirect('signup')
        else:
            messages.error(request,"Terjadi kesalahan!")    
            return redirect('signup')
    else:
        form = UserCreationForm()
        konteks = {
            'form':form,
        }
        return render(request,'perpustakaan/signup.html',konteks)

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def index(request):
    books = Buku.objects.all()

    context = {
        'title':'Perpustakaan',
        'subtitle':'Selamat Datang di Perpustakaan',
        'books':books
    }
    return render(request,'perpustakaan/index.html',context)

#create
@login_required(login_url=settings.LOGIN_URL)
def tambah_buku(request):
    if request.POST:
        form = FormBuku(request.POST)
        if form.is_valid():
            form.save()
            pesan = 'Input Buku Telah Tersimpan'
            form = FormBuku()
            konteks = {
                'form':form,
                'pesan':pesan,
            }
            return render(request,'perpustakaan/tambah-buku.html',konteks)
    else:
        form = FormBuku
        konteks = {
            'form':form,
        }
        return render(request,'perpustakaan/tambah-buku.html',konteks)

#
@login_required(login_url=settings.LOGIN_URL)
def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'perpustakaan/ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST, instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil diperbaharui!")
            return redirect('ubah_buku', id_buku=id_buku) 
    else:
        form = FormBuku(instance=buku)
        konteks = {
            'form':form,
            'buku':buku,
        }
        return render(request, template, konteks)



@login_required(login_url=settings.LOGIN_URL)
def hapus_buku(request, id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    messages.success(request,"Data Berhasi dihapus!")
    return redirect('buku')
    