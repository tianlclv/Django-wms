# coding=utf8
from django.shortcuts import render
from django.http import HttpResponseRedirect

from orders.forms import UserForm, AddressForm
from orders import models
from .models import Address

import json


def index(request):
    return render(request, 'orders/index.html')


def order(request):
    return render(request, 'orders/order.html')


def userlist(request):
    user_lists = models.Luser.objects.all()
    return render(request, 'orders/userlist.html', {'user_lists': user_lists})


def adduser(request):

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            address_area = request.POST.get('address_area')
            address_province = request.POST.get('address_province')
            address_city = request.POST.get('address_city')
            address_class = request.POST.get('address_class')
            address_full = request.POST.get('address_full')

            joe=Address.objects.get(address_full=user_address)

            form.save()
            form.address_full.add(joe)
            form.save()
            return HttpResponseRedirect('./adduser.html')
        else:
            user_error = form.errors
            return render(request, 'orders/adduser.html', {'form': form, 'errors': user_error})
    else:
        form = UserForm()

    return render(request, 'orders/adduser.html', {'form': form})


def address(request):
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address_area = request.POST.get('address_area')
            address_province = request.POST.get('address_province')
            address_city = request.POST.get('address_city')
            address_class = request.POST.get('address_class')
            address_full = request.POST.get('address_full')
            
            form.save()
            return render(request, 'orders/address.html', {'form':form})
    else:
        form = AddressForm()
        
    return render(request, 'orders/address.html', {'form':form})

def product(request):
    return render(request, 'orders/product.html')
