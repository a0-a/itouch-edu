from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Category, Photo

# Create your views here.
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'gallery.html', context)

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, 'photo.html', {'photo':photo})

def addPhoto(request):
    categories = Category.objects.all()
    
    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image,
        )  

        return redirect('gallery')       

    context = {'categories': categories}
    return render(request, 'add.html', context)      


