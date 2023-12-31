# Generated by Django 4.2.2 on 2023-07-04 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FooterLinkBox',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
            ],
            options={
                'verbose_name': 'دسته بندی لینک های فوتر',
                'verbose_name_plural': 'دسته بندی های لینک های فوتر',
            },
        ),
        migrations.CreateModel(
            name='SiteBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='نام بنر')),
                ('url', models.URLField(blank=True, max_length=400, null=True, verbose_name='آدرس بنر')),
                ('file', models.FileField(upload_to='images/banners', verbose_name='تصویر')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال / غیر فعال')),
                ('positions', models.CharField(choices=[('blog', 'بلاگ'), ('article_detail', 'صفحه جزییات مقاله'), ('blog_category', 'صفحه دسته بندی بلاگ'), ('blog_tag', 'صفحه برچسب های بلاگ'), ('python_course', 'ٌصفحه درس پایتون')], max_length=200, verbose_name='جایگاه قرار گیری')),
            ],
            options={
                'verbose_name': 'بنر تبلیغاتی',
                'verbose_name_plural': 'بنرهای تبلغاتی',
            },
        ),
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_main_setting', models.BooleanField(verbose_name='تنطیمات اصلی')),
                ('site_name', models.CharField(max_length=200, verbose_name='نام سایت')),
                ('logo', models.ImageField(upload_to='site-setting', verbose_name='لوگوی درس های پایتون')),
                ('logo_blog', models.ImageField(blank=True, null=True, upload_to='site-setting', verbose_name='لوگوی بلاگ')),
                ('logo_main_page', models.ImageField(blank=True, null=True, upload_to='site-setting', verbose_name='لوگوی صفحه اصلی')),
                ('site_url', models.CharField(max_length=200, verbose_name='دامنه')),
                ('address', models.CharField(max_length=200, verbose_name='آدرس')),
                ('phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='شماره تماس')),
                ('email', models.CharField(blank=True, max_length=200, null=True, verbose_name='ایمیل')),
                ('about_us_text', models.TextField(max_length=200, verbose_name='درباره ما')),
                ('copy_right_text', models.TextField(verbose_name='متن کپی رایت')),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات',
            },
        ),
        migrations.CreateModel(
            name='FooterLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url', models.URLField(max_length=500, verbose_name='لینک')),
                ('footer_link_box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_module.footerlinkbox', verbose_name='دسته بندی')),
            ],
            options={
                'verbose_name': 'لینک های فوتر',
                'verbose_name_plural': 'لینک های فوتر',
            },
        ),
    ]
