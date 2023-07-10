from django.db import models
from django.conf import settings

# Create your models here.


class SiteSetting(models.Model):
    is_main_setting = models.BooleanField(verbose_name='تنطیمات اصلی')
    site_name = models.CharField(max_length=200, verbose_name='نام سایت')
    logo = models.ImageField(upload_to='images/site-logo', verbose_name='لوگو')

    site_url = models.CharField(max_length=200, verbose_name='دامنه')
    address = models.CharField(max_length=200, verbose_name='آدرس')
    phone = models.CharField(max_length=200, verbose_name='شماره تماس', null=True, blank=True)
    email = models.CharField(max_length=200, verbose_name='ایمیل', null=True, blank=True)
    about_us_text = models.TextField(max_length=200, verbose_name='درباره ما')
    copy_right_text = models.TextField(verbose_name='متن کپی رایت')

    class Meta:
        verbose_name = 'تنظیمات سایت'
        verbose_name_plural = 'تنظیمات'

    def __str__(self):
        return self.site_name


class FooterLinkBox(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')

    class Meta:
        verbose_name = 'دسته بندی لینک های فوتر'
        verbose_name_plural = 'دسته بندی های لینک های فوتر'

    def __str__(self):
        return self.title


class FooterLink(models.Model):
    title = models.CharField(max_length=200, verbose_name='عنوان')
    url = models.URLField(max_length=500, verbose_name='لینک')
    footer_link_box = models.ForeignKey(to=FooterLinkBox, on_delete=models.CASCADE, verbose_name='دسته بندی')

    class Meta:
        verbose_name = 'لینک های فوتر'
        verbose_name_plural = 'لینک های فوتر'

    def __str__(self):
        return self.title


class SiteBanner(models.Model):

    class SiteBannerPositions(models.TextChoices):
        blog = 'blog', 'بلاگ',
        article_detail = 'article_detail', 'صفحه جزییات مقاله',
        blog_category = 'blog_category', 'صفحه دسته بندی بلاگ',
        blog_tag = 'blog_tag', 'صفحه برچسب های بلاگ',
        main_page = 'main_page', 'صفحه اصلی'


    title = models.CharField(max_length=200, verbose_name='نام بنر')
    url = models.URLField(max_length=400, null=True, blank=True, verbose_name='آدرس بنر')
    file = models.FileField(upload_to='images/banners', verbose_name='تصویر')
    is_active = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    positions = models.CharField(max_length=200, choices=SiteBannerPositions.choices, verbose_name='جایگاه قرار گیری')


    def __str__(self):
        return self.title


    class Meta:

        verbose_name = 'بنر تبلیغاتی'
        verbose_name_plural = 'بنرهای تبلغاتی'