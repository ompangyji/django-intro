from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):
    username = '정연지'

    result = {
        'username': username,
    }

    return render(request, 'hello.html', result)

def cube(request, num):
    result = {
        'num': num,
        'cube': int(num)**3, 
    }
    return render(request, 'cube.html', result)