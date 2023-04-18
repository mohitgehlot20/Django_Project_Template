from django.contrib.auth import authenticate, login
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import Employee
# from app.models import Employees
from newapp.models import *
from django.core import paginator


# Create your views here.
def index(request):
    emp = Employee.objects.all()
    paginator = Paginator(emp, 4)
    page = request.GET.get('page')
    emp = paginator.get_page(page)
    context = {
        'emp': emp,
    }
    return render(request, "index.html", context)


def ADD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        emp.save()
        return redirect('home')
    return render(request, "index.html")


def edit(request):
    emp = Employee.objects.all()

    context = {
        'emp': emp
    }
    return redirect(request, 'index.html', context)


def update(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        emp = Employee(
            id=id,
            name=name,
            email=email,
            address=address,
            phone=phone,
        )
        emp.save()
        return redirect('home')

    return redirect(request, 'index.html')


def delete(request, id):
    emp = Employee.objects.filter(id=id).delete()
    context = {
        'emp': emp
    }
    return redirect('home')

#          ===========Not using this=============
# def my_view(request):
#     # Fetch data for table
#     # Replace this with your actual data fetching logic
#     data = Employee.objects.all()
#
#     # Configure Paginator
#     paginator = Paginator(data,2)  # 10 items per page
#
#     page = request.GET.get('page')
#     items = paginator.get_page(page)
#
#     return render(request, 'index.html', {'items': items})


# def search(request):
#     emp = Employee.objects.all()
#     if request.method=="GET":
#         st=request.GET.get('searchname')
#         if st!=None:
#             emp=Employee.objects.filter(name=st)
#         context = {
#             'emp': emp,
#         }
#         return render(request, "index.html", context)

def get_user_by_id(request):
    if request.method == 'GET':
        search_id = request.GET.get('searchname', '')
        try:
            emp = Employee.objects.get(id=search_id)
            context = {'emp': emp}
        except Employee.DoesNotExist:
            context = {'error': 'User not found.'}
        return render(request, 'user_detail.html', context)


# def loginUser(request):
#     if request.method=="POST":
#         username=request.POST.get('username')
#         password=request.POST.get('password')
#         user=authenticate(username=username,password=password)
#         if user is not None:
#             login(request,user)
#             return redirect("/")
#         else:
#             return render(request,'login.html')
#     return render(request, 'login.html')

def get_user_by_name(request):
    if request.method == 'GET':
        search_name = request.GET.get('searchname', '')
        try:
            emp = Employee.objects.get(name=search_name)
            context = {'emp': emp}
        except Employee.DoesNotExist:
            context = {'error': 'User not found.'}
        return render(request, 'user_detail.html', context)


