from django import forms
from django.forms import ModelForm, TextInput
from orders.models import Order, Luser, Track, Product, Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = "__all__"


class UserForm(forms.ModelForm):

    class Meta:
        model = Luser
        fields = "__all__"
        # 新增用户输入框美化
        widgets = {
            'user_name': TextInput(attrs={'class': 'form-control', 'placeholder': '姓名'}),
            'user_qq': TextInput(attrs={'class': 'form-control', 'placeholder': 'QQ号'}),
            'user_weixin': TextInput(attrs={'class': 'form-control', 'placeholder': '微信号'}),
            'user_phone': TextInput(attrs={'class': 'form-control', 'placeholder': '手机号码'}),
            'user_taobao': TextInput(attrs={'class': 'form-control', 'placeholder': '淘宝账号'}),
            'user_weibo': TextInput(attrs={'class': 'form-control', 'placeholder': '微博号'}),
            'user_email': TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }
        # 提示错误信息
        error_messages = {
            'user_email': {'invalid': ("输入正确的邮箱地址"), },
        }
