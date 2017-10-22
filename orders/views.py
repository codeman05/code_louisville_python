from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect

from . import models
from . import forms


def order_list(request):
    orders = models.Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})


def order_form(request):
    form = forms.OrderForm()
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            # Process form. Allow only cleaned data.
            new_order = form.save(commit=False)
            new_order.company = form.cleaned_data['company']
            new_order.name = form.cleaned_data['name']

            # Manipulate data.
            new_order.job_number = '17-0010'
            new_order.email = 'hardcoded-email.com'

            # Save data to database.
            new_order.save()
            #new_order.save_m2m()

            return HttpResponseRedirect(reverse('orders:form'))
    return render(request, 'orders/order_form.html', {'form': form})


def order_detail(request, order_pk):
    order = models.Order.objects.get(pk=order_pk)
    print(order)
    form = forms.OrderForm(request.POST, instance=order)
    # if request.method == 'POST':
    #     form = forms.OrderForm(request.POST)
    #     if form.is_valid():
    #         # Process form. Allow only cleaned data.
    #         new_order = form.save(commit=False)
    #         new_order.company = form.cleaned_data['company']
    #         new_order.name = form.cleaned_data['name']
    #
    #         # Manipulate data.
    #         new_order.job_number = '17-0010'
    #         new_order.email = 'hardcoded-email.com'
    #
    #         # Save data to database.
    #         new_order.save()
    #         #new_order.save_m2m()
    #
    #         return HttpResponseRedirect(reverse('orders:form'))
    return render(request, 'orders/order_form.html', {'form': form})

