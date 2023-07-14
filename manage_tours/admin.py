from django.contrib import admin
from jalali_date import date2jalali, datetime2jalali

from . import models
from jalali_date.admin import ModelAdminJalaliMixin, StackedInlineJalaliMixin, TabularInlineJalaliMixin





# Register your models here.
class TourFlightInline(StackedInlineJalaliMixin, admin.StackedInline):
    model = models.Flight
    extra = 2

# class TourImageGalleryInline(admin.StackedInline):
#     model = models.TourImageGallery
#     extra = 5


# class TourItineraryInline(admin.StackedInline):
#     model = models.Itinerary
#     extra = 3

# class TourIFAQInline(admin.StackedInline):
#     model = models.FAQ
#     extra = 5

class TourAdmin( ModelAdminJalaliMixin, admin.ModelAdmin):
    list_display = ['title', 'main_image', 'status', 'price']
    list_filter = ['price', 'status']
    inlines = [TourFlightInline]

    @admin.display(description='تاریخ رفت', ordering='departure_date')
    def get_departure_date_jalali(self, obj):
        return date2jalali(obj.departure_date).strftime('%y/%m/%d')

    @admin.display(description='تاریخ برگشت', ordering='return_date')
    def get_return_date_jalali(self, obj):
        return date2jalali(obj.return_date).strftime('%y/%m/%d')



admin.site.register(models.Feature)
admin.site.register(models.RefundPolicyForHotel)
admin.site.register(models.Accommodation)
admin.site.register(models.RefundPolicyForFlight)
admin.site.register(models.Flight)
admin.site.register(models.Itinerary)
admin.site.register(models.ItineraryDetail)
admin.site.register(models.FAQ)
admin.site.register(models.Tour, TourAdmin)
admin.site.register(models.TourImageGallery)


