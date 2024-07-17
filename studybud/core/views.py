from django.shortcuts import render

data = [
    {'id':1, 'name':'lets learn python'},
    {'id':2 , 'name':'Design with me'},
    {'id':3,'name':'Frontend developer'},
]

def home(request):
    context={'data':data}
    return render(request,'core/home.html',context )

def screen(request,pk):
    return render(request,'core/screen.html')
