# coding=utf8
from django.shortcuts import render
from django.http import HttpResponseRedirect

from orders.forms import UserForm, AddressForm
from orders import models


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
            user_name = form.cleaned_data['user_name']
            user_qq = form.cleaned_data['user_qq']
            user_weixin = form.cleaned_data['user_weixn']
            user_phone = form.cleaned_data['user_phone']
            user_taobao = form.cleaned_data['user_taobao']
            user_email = form.cleaned_data['user_email']
            form.save()
            return HttpResponseRedirect('./address.html')
    else:
        form = AddressForm()
    return render(request, 'orders/address.html', {'form': form})


def product(request):
    return render(request, 'orders/product.html')
