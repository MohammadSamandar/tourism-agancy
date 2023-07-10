from django.urls import path
from . import views

urlpatterns = [
    path('tour-list/', views.tour_list, name='tour-list'),
    path('<slug:slug>', views.tour_detial, name='tour-detail'),
    path('tour-booking/', views.tour_booking, name='tour-booking'), # صفحه پرداخت
    path('tour-search-result/', views.tour_search_result, name='tour-search-result'),


]