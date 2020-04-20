from django.shortcuts import render, get_object_or_404
from .models import Order

# Create your views here.

def detail(request, id):
    order = get_object_or_404(Order, pk=id)
    return render(request, "samplecustomer/detail.html", {"order":order})