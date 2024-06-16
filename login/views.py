from django.shortcuts import render

from django.http import HttpResponse

from django.template import loader

from .models import usertable
# def login(request):
#     return HttpResponse('Hello World')

# def login(request):
#     template = loader.get_template('sign.html')
#     return HttpResponse(template.render())

def login(request):
    if request.method == "POST":

        name = request.POST.get('username')
        email = request.POST.get('Email')
        password = request.POST.get('Password')
        

        data=usertable.objects.create(Username = name,Email=email,Password=password)
        data.save()
        return render(request, 'sign.html')
    
    elif request.method == "GET":
        return render(request,'sign.html')
    
    # return HttpResponse(render,'sign.html')

