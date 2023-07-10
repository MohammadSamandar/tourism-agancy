from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Tour
# Create your views here.


def tour_list(request):

    tours = Tour.objects.all().order_by('price')

    context = {
        'tours': tours,
    }


    return render(request, 'manage_tours/tour-list.html', context)


def tour_detial(request, slug):

    tour = get_object_or_404(Tour, slug=slug)

    context = {
        'tour': tour,
    }


    return render(request, 'manage_tours/tour-details.html', context)

def tour_booking(request):

    tours = Tour.objects.all()

    context = {
        'tour': tours,
    }


    return render(request, 'manage_tours/tour-booking.html', context)



def tour_search_result(request):

    tours = Tour.objects.all()

    context = {
        'tour': tours,
    }


    return render(request, 'manage_tours/tour-search-result.html', context)