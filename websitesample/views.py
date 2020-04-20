from django.shortcuts import render

from django.http import HttpResponse


from samplecustomer.models import Agent, Customer, Order

# Create your views here.


def welcome(request):
    return render(request, "websitesample/welcome.html",
    {"num_agents": Agent.objects.count(), "num_customers": Customer.objects.count(), "num_orders": Order.objects.count}
    )


