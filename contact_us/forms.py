from django import forms
from .models import ContactUs


class ContactUsModelForm(forms.ModelForm):

    class Meta:
        model = ContactUs
        fields = ['full_name', 'email','message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'InputName', 'placeholder': 'نام کامل'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control', 'id': 'InputEmail', 'placeholder': 'ایمیل تان را وارد کنید'
            }),

            'message': forms.Textarea(attrs={
                'class': 'message-control form-control', 'id': 'InputMessage', 'placeholder': 'پیام خود وارد کنید'
            }),

        }

        error_messages = {
            'full_name': {
                'required': 'نام و نام خانوادگی اجباری میباشد لطفا وارد کنید'
            },
            'Email': {
                'required': 'ایمیل اجباری میباشد لطفا وارد کنید'
            },

            'message': {
                'required': 'متن پیام اجباری میباشد لطفا وارد کنید'
            }
        }


