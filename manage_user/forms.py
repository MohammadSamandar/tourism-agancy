from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


phone_regex = RegexValidator(regex=r'^\+?1?\d{0,11}$',
                                 message="Phone number must be entered in the format: '+981111111111'. Up to 11 digits allowed.")



class RegisterForm(forms.Form):
    username = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={
            'class': 'form-control form-group',
            'placeholder': 'نام کاربری',


        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ],

    )

    email = forms.EmailField(
        label= 'ایمیل',
        widget= forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل',

        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ],

    )

    mobile = forms.CharField(max_length=11,
        label= 'موبایل',
        widget= forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'موبایل',

        }),
        validators=[
            phone_regex,
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ],

    )
    password = forms.CharField(
        label= 'کلمه عبور',
        widget = forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'رمز عبور',

        }),
        validators=[
            validators.MaxLengthValidator(100),
        ],

    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'تکرار رمز عبور',

        }),
        validators=[
            validators.MaxLengthValidator(100),
        ],
    )



    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')


        if password == confirm_password:
            return confirm_password


        raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')



class LoginForm(forms.Form):
    email = forms.EmailField(
        label= 'ایمیل',
        widget= forms.EmailInput(attrs={
            'class': 'form-control bg-transparent',
            'placeholder': 'ایمیل',
            'autocomplete': 'off',
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ],

    )
    password = forms.CharField(
        label= 'کلمه عبور',
        widget = forms.PasswordInput(attrs={
            'class': 'form-control bg-transparent',
            'placeholder': 'رمز عبور'
        }),
        validators=[
            validators.MaxLengthValidator(100)
        ],

    )


class RecoveryPasswordForm(forms.Form):
    email = forms.EmailField(
        label= 'ایمیل',
        widget= forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل خود را وارد کنید',
        }),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ],
    )



class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control bg-transparent',
            'placeholder': 'رمز عبور',
            'autocomplete': 'off',
        }),
        validators=[
            validators.MaxLengthValidator(100),
        ],

    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control bg-transparent',
            'placeholder': 'تکرار رمز عبور',
            'autocomplete': 'off',
        }),
        validators=[
            validators.MaxLengthValidator(100),
        ],
    )

