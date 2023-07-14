from django.db import models
from tinymce.models import HTMLField



class Feature(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'امکانات اقامتگاه'
        verbose_name_plural = 'امکانات اقامتگاه ها'

class RefundPolicyForHotel(models.Model):
    penalty_amount = models.DecimalField(max_digits=10, decimal_places=2)
    cancellation_notice_period = models.IntegerField()

    def __str__(self):
        return f"قوانین استرداد هتل - جریمه: {self.penalty_amount}, زمان اعلام کنسلی: {self.cancellation_notice_period} روز"


    class Meta:
        verbose_name = 'قوانین استرداد هتل'
        verbose_name_plural = 'قوانین استرداد هتل ها'

class Accommodation(models.Model):
    Meta_Tags_TYPE_CHOICES = [
        ('Hotel', 'هتل'),
        ('Apartment', 'آپارتمان'),
        ('Suite ', 'سوییت'),

    ]

    type = models.CharField(
        max_length=12,
        choices=Meta_Tags_TYPE_CHOICES,
        default='Hotel',
        verbose_name='نوع محل اقامت'
    )

    # فیلدهای مشترک بین تمام اقامتگاه‌ها
    name = models.CharField(max_length=250, verbose_name='نام اقامتگاه', null=True , blank=True)
    city = models.CharField(max_length=250, verbose_name='شهر', null=True , blank=True)
    address = models.CharField(max_length=200, verbose_name='آدرس')
    features = models.ManyToManyField('Feature', blank=True)
    number_of_rooms = models.IntegerField(verbose_name='تعداد اتاق', null=True, blank=True)

    # ویژگی‌های خاص هر نوع محل اقامت
    hotel_stars = models.IntegerField(null=True, blank=True)
    refund_policy = models.OneToOneField('RefundPolicyForHotel', on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name



    class Meta:
        verbose_name = 'اقامتگاه'
        verbose_name_plural = 'اقامتگاه ها'

class TourImageGallery(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان تصویر')
    image = models.ImageField(upload_to='images/tour-image', verbose_name='تصویر')


    def __str__(self):
        return f"گالری تصاویر {self.title}"


    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = 'تصاویر'



class ItineraryDetail(models.Model):
    place = models.CharField(max_length=100, verbose_name='نام مکان')
    day = models.IntegerField(verbose_name='روز چندم')
    short_description = HTMLField(verbose_name='توضیحات کوتاه')

    def __str__(self):
        return f"جزییات {self.place}"


    class Meta:
        verbose_name = 'جزییات برنامه سفر'
        verbose_name_plural = 'جزییات برنامه های سفر'


class Itinerary(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان', null=True, blank=True)
    detail = models.ManyToManyField(ItineraryDetail, verbose_name='جزییات')


    def __str__(self):
        return f"برنامه سفر {self.title}"


    class Meta:
        verbose_name = 'برنامه سفر'
        verbose_name_plural = 'برنامه های سفر'


class FAQ(models.Model):
    question = models.CharField(max_length=100, verbose_name='سوال')
    answer = models.TextField(max_length=450, verbose_name='جواب')

    def __str__(self):
        return self.question


    class Meta:
        verbose_name = 'سوالات متداول'
        verbose_name_plural = 'سوالات متداول'




class Tour(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان', null=True, blank=True)
    slug = models.SlugField(default="", null=False, blank=True, db_index=True, max_length=200, unique=True)
    description = HTMLField(verbose_name='توضیحات', null=True, blank=True)
    main_image = models.ImageField(upload_to='images/tour-image', verbose_name='تصویر اصلی', blank=True, null=True)
    video = models.FileField(upload_to='video/tour',  verbose_name='ویدیو تور', null=True, blank=True)
    status = models.BooleanField(default=False, verbose_name='فعال / غیر فعال')
    location = models.TextField(verbose_name='مکان تور در نقشه', null=True, blank=True)
    duration = models.CharField(max_length=100, verbose_name='مدت زمان', null=True, blank=True)

    origin = models.CharField(max_length=100,verbose_name='مبدا')
    destination = models.CharField(max_length=100, verbose_name='مقصد')

    departure_date = models.DateTimeField(verbose_name='تاریخ رفت')
    return_date = models.DateTimeField(verbose_name='تاریخ برگشت')

    accommodation = models.ManyToManyField(Accommodation, verbose_name='اطلاعات اقامتگاه')
    itinerary = models.ManyToManyField(Itinerary, verbose_name='برنامه سفر', null=True, blank=True)
    faq = models.ManyToManyField(FAQ, verbose_name='سوالات متداول', null=True, blank=True)
    image_gallery = models.ManyToManyField(TourImageGallery, verbose_name='گالری تصویر')
    # flight = models.OneToOneField(Flight, on_delete=models.CASCADE, verbose_name='اطلاعات پرواز')

    rating = models.IntegerField(verbose_name='امتیاز')
    seller = models.CharField(max_length=100, verbose_name='فروشنده تور')
    services = models.TextField(verbose_name='خدمات تور')

    price = models.IntegerField(verbose_name='قیمت تور')



    def __str__(self):
        return f"Tour {self.title}"

    class Meta:
        verbose_name = 'تور'
        verbose_name_plural = 'تور ها'









class Flight(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE, verbose_name='تور', null=True, blank=True)

    FLIGHT_TYPES = [
        ('one_way', 'رفت'),
        ('round_trip', 'برگشت'),
    ]

    flight_type = models.CharField(max_length=20, choices=FLIGHT_TYPES, verbose_name='نوع پرواز')
    flight_number = models.CharField(max_length=50, verbose_name='شماره پرواز')

    airport_of_origin = models.CharField(max_length=100, verbose_name='فرودگاه مبدا')
    destination_airport = models.CharField(max_length=100, verbose_name='فرودگاه مقصد')

    luggage_count = models.PositiveIntegerField(verbose_name='تعداد چمدان', null=True, blank=True)
    luggage_weight = models.DecimalField(max_digits=5, decimal_places=2, verbose_name='بار چمدان')


    departure_date = models.DateField(verbose_name='تاریخ حرکت')
    arrival_date = models.DateField(verbose_name='تاریخ رسیدن')

    departure_time  = models.TimeField(verbose_name='ساعت حرکت')
    arrival_time = models.TimeField(verbose_name='ساعت رسیدن')

    airline = models.CharField(max_length=100, verbose_name='شرکت هواپیمایی')
    cabin_type = models.CharField(max_length=50, verbose_name='نوع کابین', blank=True, null=True)
    fare_class = models.CharField(max_length=50, verbose_name='کلاس نرخی' , null=True, blank=True)
    refund_policy = models.OneToOneField('RefundPolicyForFlight', on_delete=models.CASCADE, verbose_name='قوانین استرداد پرواز', blank=True, null=True, )



    def __str__(self):
        return self.flight_type


    class Meta:
        verbose_name = 'پرواز'
        verbose_name_plural = 'پرواز ها'



class RefundPolicyForFlight(models.Model):
    penalty_amount = models.DecimalField(max_digits=10, decimal_places=2)
    cancellation_notice_period = models.IntegerField()

    def __str__(self):
        return f"قوانین استرداد پرواز - جریمه: {self.penalty_amount}, زمان اعلام کنسلی: {self.cancellation_notice_period} روز"

    class Meta:
        verbose_name = 'قوانین استرداد پرواز'
        verbose_name_plural = 'قوانین استرداد پرواز'
