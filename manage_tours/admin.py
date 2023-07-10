from django.contrib import admin
from . import models

# Register your models here.

class TourImageGalleryInline(admin.TabularInline):
    model = models.TourImageGallery
    extra = 5


class TourItineraryInline(admin.TabularInline):
    model = models.Itinerary
    extra = 5

class TourIFAQInline(admin.TabularInline):
    model = models.FAQ
    extra = 5

class TourAdmin(admin.ModelAdmin):
    list_display = ['title', 'main_image', 'status', 'price']
    list_filter = ['price', 'status']
    inlines = [TourImageGalleryInline, TourItineraryInline, TourIFAQInline]


admin.site.register(models.Feature)
admin.site.register(models.RefundPolicyForHotel)
admin.site.register(models.Accommodation)
admin.site.register(models.RefundPolicyForFlight)
admin.site.register(models.Flight)
admin.site.register(models.Itinerary)
admin.site.register(models.FAQ)
admin.site.register(models.Tour, TourAdmin)
admin.site.register(models.TourImageGallery)


