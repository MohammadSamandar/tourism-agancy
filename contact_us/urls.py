from django.urls import path
from . import views
# from django.views.generic import

urlpatterns = [
    # path('', views.contact_us_page, name='contact_us_page'),
    path('', views.contact_us_view.as_view(), name='contact_us_page'),

]