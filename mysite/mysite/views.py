'''
Created on 2018. 1. 14.

@author: HO
'''
from django.views.generic.base import TemplateView
 
class HomeView(TemplateView):
    template_name = 'home.html'