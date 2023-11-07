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
        'stripe_public_key': 'pk_test_51O9m4RJck8aA9DpqIeVuLhc34WmnU3em0Xam42wnd9f2UTqOJOSqbVVbfGktKO6iReQ8Npa9PmqCf2HX6KfFNt8a00gTkxWMVf',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
