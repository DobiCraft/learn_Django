'''
Created on 2018. 1. 16.

@author: HO
'''
from django import forms

class PostSearchForm(forms.Form):
    search_word = forms.CharField(label='Search Word')
    