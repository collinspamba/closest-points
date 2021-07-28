"""application Views
"""
from django.shortcuts import render

def homepage(request):
    """homepage
    """
    return render(request, 'application/home.html')
