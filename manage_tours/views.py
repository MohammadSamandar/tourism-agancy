from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tour, Itinerary, ItineraryDetail


# Create your views here.


def tour_list(request):

    tours = Tour.objects.filter(status=True).order_by('price')

    context = {
        'tours': tours,
    }


    return render(request, 'manage_tours/tour-list.html', context)


def tour_detail(request, slug):
    tour = get_object_or_404(Tour, slug=slug)
    itinerary_details = ItineraryDetail.objects.filter(itinerary__tour=tour).order_by('day')

    context = {
        'tour': tour,
        'itinerary_details': itinerary_details
    }

    return render(request, 'manage_tours/tour-details.html', context)


def tour_booking(request):

    tours = Tour.objects.all()

    context = {
        'tour': tours,
    }


    return render(request, 'manage_tours/tour-booking.html', context)



def tour_search_result(request):
    tours = Tour.objects.filter(status=True).order_by('price')

    context = {
        'tours': tours,
    }

    return render(request, 'manage_tours/search-result.html', context)