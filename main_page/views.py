from django.shortcuts import render

from manage_tours.models import Tour


# Create your views here.

def main_page(request):
    tours = Tour.objects.filter(status=True).order_by('price')[0:5]

    context = {
        'tours': tours,
    }

    return render(request, 'main_page/index7.html', context)












def register_modal_component(request):

    return render(request, 'register_component.html')


def login_modal_component(request):

    return render(request, 'login_component.html')


def header_component(request):

    return render(request, 'site_header_component.html')


def footer_component(request):

    return render(request, 'site_footer_component.html')