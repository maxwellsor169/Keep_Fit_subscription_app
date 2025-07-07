from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Ri8wN2KEg0zizs07P7HC0WrGWubVenNoSulm1Kt8laBLjuVVV9rMGnXvsFLnqCX0py4SO5A3K8p39smQ2nK0QxY00bEkt6L3P',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)