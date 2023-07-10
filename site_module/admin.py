from django.contrib import admin
from .models import SiteSetting, FooterLinkBox, FooterLink, SiteBanner
# Register your models here.

class FooterLinkAdmin(admin.ModelAdmin):
    list_display = ['title', 'url']

class SiteBannerAdmin(admin.ModelAdmin):

    list_display = ['title', 'url', 'positions']


admin.site.register(SiteSetting)
admin.site.register(SiteBanner, SiteBannerAdmin)
admin.site.register(FooterLinkBox)
admin.site.register(FooterLink, FooterLinkAdmin)