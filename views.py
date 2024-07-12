from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
# def index_page(request):
#     return render(request,'home_module/index_page.html')

class HomePageView(TemplateView):
    template_name = 'home_module/index_page.html'


def site_header_component(request):
    context = {
        'link': 'آموزش جنگو'
    }
    return render(request, 'shared/site_header_component.html', context)


def site_footer_component(request):
    return render(request, 'shared/site_footer_component.html', {})