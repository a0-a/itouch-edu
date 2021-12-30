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

def user_gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'user_gallery.html', context)

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

        return redirect('user_gallery')       

    context = {'categories': categories}
    return render(request, 'add.html', context)      


def register(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        pasword2 = request.POST['password2']

        if password == pasword2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email has taken please use another one')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'password is\'nt matching')
            return redirect('register')  
        return redirect('/')   
    else:           
        return render(request, 'signup.html')

def login(request):


    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('user_gallery')
        else:
            messages.info(request, 'invalid: email or password')
            return redirect('login')  
    else:
        return render(request, 'login.html')  



def logout(request):
    auth.logout(request)
    return redirect('login')