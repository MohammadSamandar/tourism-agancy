from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from manage_user.forms import RegisterForm, LoginForm, RecoveryPasswordForm, ResetPasswordForm
from .models import CustomUser
from django.utils.crypto import get_random_string
from django.http import Http404, HttpRequest
from django.contrib.auth import login, logout
from .email_service import send_email
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth import authenticate, login




class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        context = {
            'register_form': register_form,
        }
        return render(request, 'register_component.html', context)

    def post(self, request):
        user_name = request.POST.get('username')
        user_email = request.POST.get('email')
        user_password = request.POST.get('password')
        confirm_password = request.POST.get('passwordconfirm')
        user = CustomUser.objects.filter(email__iexact=user_email, username__iexact=user_name).exists()
        errors = {}

        if user:
            errors['email'] = 'کاربری با این ایمیل و نام کاربری قبلاً ثبت نام کرده است'
        elif user_password != confirm_password:
            errors['password'] = 'کلمه عبور و تکرار کلمه عبور مغایرت دارند'
            # raise ValidationError('کلمه عبور و تکرار کلمه عبور مغایرت دارند')

        else:

            new_user = CustomUser(email=user_email, email_active_code=get_random_string(72),
                                      is_active=False, username=user_name,)
            new_user.set_password(user_password)
            new_user.save()
            send_email('فعال سازی حساب کاربری', new_user.email, {'user': new_user}, 'manage_user/email/active_accounts.html')
            return JsonResponse({'message': 'ایمیل فعال سازی حساب کاربری برای شما ارسال شد. ایمیل خود را چک نمایید'})
            # return redirect(reverse('login_page'))

        return JsonResponse({'errors': errors})




class ActivateAccountView(View):
    def get(self, request, email_active_code):

        user = CustomUser.objects.filter(email_active_code__iexact=email_active_code).first()
        if user is not None:
            if not user.is_active:
                user.is_active = True
                user.email_active_code = get_random_string(72)
                user.save()

                login(request, user)

                return redirect(reverse('main-page'))
            else:
                # نمایش پیام "حساب کاربری شما فعال شده است" به کاربر
                pass

        raise Http404


class LoginView(View):

    def get(self, request):
        login_form = LoginForm()
        context = {
            'login_form': login_form
        }

        return render(request, 'login_component.html', context)

    def post(self, request: HttpRequest):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_email = request.POST.get('email')
            user_password = request.POST.get('password')
            user: CustomUser = CustomUser.objects.filter(email__iexact=user_email).first()

            if user is not None: # اگر کاربر وجود داره
                if not user.is_active: # اگر حساب کاربری فعال نیست
                     # show error
                     errors['error_account_active'] = 'حساب کاربری شما فعال نشده است'

                else:
                    is_password_correct = user.check_password(user_password) # مقایسه پسورد وارد شده در فرم و پسورد موجود در دیتابیس
                    if is_password_correct: # اگر پسورد درست بود یا در دیتابیس موجود بود
                        login(request, user) # لاگین انجام بشود
                        return redirect(reverse('main-page')) # بعد از لاگین به این صفحه ریدایرکت بشود
                    else: # اگر پسورد وارد شده درست نبود
                        errors['password_error'] = 'نام کاربری یا کلمه عبور اشتباه است'

            else: # اگر کاربر وجود نداره
                errors['user_error'] = 'نام کاربری یا کلمه عبور اشتباه است'

        return JsonResponse({'errors': errors})



class RecoveryPassword(View):
    def get(self, request):
        recovery_pass_form = RecoveryPasswordForm()
        context = {
            'recovery_pass_form': recovery_pass_form,
            'message': None
        }
        return render(request, 'manage_user/recovery_password.html', context)

    def post(self, request):
        recovery_pass_form = RecoveryPasswordForm(request.POST)
        if recovery_pass_form.is_valid():
            user_email = recovery_pass_form.cleaned_data.get('email')
            user: CustomUser = CustomUser.objects.filter(email__iexact=user_email).first()

            if user is not None:
                send_email('بازیابی کلمه عبور', user.email, {'user': user}, 'manage_user/email/forgot_password.html')
                message = 'ایمیل بازیابی رمز عبور با موفقیت ارسال شد.'
            else:
                message = 'متاسفانه مشکلی در ارسال ایمیل رخ داد.'
        else:
            message = 'لطفاً فرم را به درستی پر کنید.'

        return JsonResponse({'message': message})



class ResetPassword(View):
    def get(self, request: HttpRequest, active_code):
        user: CustomUser = CustomUser.objects.filter(email_active_code__iexact=active_code).first()
        if user is None:
            return JsonResponse({'success': True, 'message': 'تغییر رمز عبور با موفقیت انجام شد. حالا از طریق دکمه "ورود" بالای صفحه میتوانید وارد حساب کاربری خود شوید'})

        reset_pass_form = ResetPasswordForm()
        response_data = {
            'error': True,
            'success': False,
            'message': 'فرم را به درستی پر کنید'
        }
        return JsonResponse(response_data)

    def post(self, request: HttpRequest, active_code):
        reset_pass_form = ResetPasswordForm(request.POST)
        user: CustomUser = CustomUser.objects.filter(email_active_code__iexact=active_code).first()
        if reset_pass_form.is_valid():
            if user is None:
                return JsonResponse({'error': True, 'message': 'کاربری وجود ندارد'})
            user_new_password = reset_pass_form.cleaned_data.get('password')
            user.set_password(user_new_password)
            user.email_active_code = get_random_string(72)
            user.is_active = True
            user.save()
            return JsonResponse({'success': True, 'message': 'تغییر رمز عبور با موفقیت انجام شد. حالا از طریق دکمه "ورود" بالای صفحه میتوانید وارد حساب کاربری خود شوید'})

        response_data = {
            'error': True,
            'success': False,
            'message': 'فرم را به درستی پر کنید'
        }
        return JsonResponse(response_data)



class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect(reverse('main-page'))


