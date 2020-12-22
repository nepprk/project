from django.shortcuts import render

def webpage1(request):
    return render(request,'index.html')

def webpage2(request):
    return render(request,'register.html')
def webpage3(request):
    return render(request,'login.html')
def webpage4(request):
    return render(request,'dashboard.html')
def webpage5(request):
    return render(request,'password.html')
