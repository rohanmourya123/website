from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.contrib.auth.decorators import login_required
from .form import signup_form,contact_form,login_form

# Create your views here.
def fun(request):
    value = Product.objects.all()

    context = {
        "value": value,

    }
    return render(request,"index.html",context=context)

@login_required(login_url="/login")
def product_detail(request,pk):
    prod_detail = Product.objects.get(pk=pk)
    context = {
        "prod_detail": prod_detail
    }
    return render(request,"detail.html",context=context)
# Create your views here.


def contact(request):
    value3=contact_form()
    context={
        'value3':value3
    }
    if request.method == 'POST':
        value3=contact_form(request.POST)
        if value3.is_valid():
            value3.save()
            return HttpResponse('Usersave')
    return render(request,'contact.html',context=context)



def signup(request):
    form1=signup_form()
    context={
        'form1':form1
    }
    if request.method == 'POST':
        user=signup_form(request.POST)
        if user.is_valid():
         user.save()
    return HttpResponse('Usersave')
    return render(request,'signup.html',context=context)


def login(request):
    s=login_form
    context={
        "prod":s
    }
    if request.method=="GET":
        name = login_form(request.GET)
        name.save()
    return render(request,"new.html",context=context)

def search(request):
    q=request.GET['q']
    prod=Product.objects.filter(name__icontains=q)
    context = {
        "value": prod
    }
    return render(request, "index.html", context=context)

