from django.shortcuts import render
from django.views.generic import TemplateView
from datetime import datetime
from .utils.age_calculator import calculate_age

# Create your views here.

def index(request):
	return render(request, 'index.html', context=None)
	
class NewcastleView(TemplateView):
	template_name = 'newcastle.html'
	
class YorkView(TemplateView):
	template_name = 'york.html'
	
class TryHackMeView(TemplateView):
	template_name = 'tryhackme.html'
	
class CPDView(TemplateView):
	template_name = 'cpd.html'
	
class COEView(TemplateView):
	template_name = 'coe.html'


def roxy_and_luna(request):
    roxy_birthday = datetime(2022, 3, 18)
    luna_birthday = datetime(2022, 7, 2)

    roxy_age_years, roxy_age_months = calculate_age(roxy_birthday)
    luna_age_years, luna_age_months = calculate_age(luna_birthday)

    return render(request, 'roxyandluna.html', {'roxy_age_years': roxy_age_years, 'roxy_age_months': roxy_age_months,
                                                 'luna_age_years': luna_age_years, 'luna_age_months': luna_age_months})
def roxy_and_luna(request):
    roxy_birthday = datetime(2022, 3, 18)
    luna_birthday = datetime(2022, 7, 2)

    roxy_age_years, roxy_age_months = calculate_age(roxy_birthday)
    luna_age_years, luna_age_months = calculate_age(luna_birthday)

    return render(request, 'roxyandluna.html', {'roxy_age_years': roxy_age_years, 'roxy_age_months': roxy_age_months,
                                                 'luna_age_years': luna_age_years, 'luna_age_months': luna_age_months})

