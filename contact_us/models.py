from django.db import models

# Create your models here.

class ContactUs(models.Model):
    full_name = models.CharField(max_length=300, verbose_name='نام و نام و خانوادگی')
    email = models.EmailField(max_length=300, verbose_name='ایمیل')
    # subject = models.CharField(max_length=300, verbose_name='موضوع')
    message = models.TextField(verbose_name='پیام')
    is_read_by_admin = models.BooleanField(verbose_name='خوانده شده توسط ادمین', default=False)
    created_date = models.DateTimeField(verbose_name='تاریخ ایجاد', auto_now_add=True)
    response = models.TextField(verbose_name='متن پاسخ', null=True, blank=True)


    class Meta:
        verbose_name = 'ارتباط با ما'
        verbose_name_plural = 'لیست ارتباط با ما'

    def __str__(self):
        return self.full_name


class UserProfile(models.Model):
    image = models.FileField(upload_to='images')