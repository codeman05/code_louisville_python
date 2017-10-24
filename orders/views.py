from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.http import HttpResponseRedirect

from . import models
from . import forms


# @login_required
def order_list(request):
    orders = models.Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})


def create_order(request):
    form = forms.OrderForm()
    if request.method == 'POST':
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            # Process form. Allow only cleaned data.
            new_order = form.save(commit=False)
            new_order.company = form.cleaned_data['company']
            new_order.name = form.cleaned_data['name']

            # Manipulate data.

            new_order.email = 'hardcoded-email.com'

            # Save data to database.
            new_order.save()
            new_order.job_number = '17-' + str(new_order.pk)
            new_order.save()
            #new_order.save_m2m()

            return HttpResponseRedirect(reverse('orders:create'))
    return render(request, 'orders/order_form.html', {'form': form})


# @login_required
def edit_order(request, order_pk):
    order = get_object_or_404(models.Order, pk=order_pk)
    form = forms.OrderForm(instance=order)
    if request.method == 'POST':
        form = forms.OrderForm(instance=order, data=request.POST)
        if form.is_valid():
            form.save()
            # Send message
            messages.success(request, "Updated order")
            return HttpResponseRedirect(reverse('orders:list'))
    return render(request, 'orders/order_form.html', {'form': form})


# @login_required
def delete_order(request, order_pk):
    order = get_object_or_404(models.Order, pk=order_pk)
    order.delete()
    return HttpResponseRedirect(reverse('orders:list'))


def combined_form(request):
    order_form = forms.OrderForm()
    test_form = forms.TestForm()
    if request.method == 'POST':
        order_form = forms.OrderForm(request.POST)
        test_form = forms.TestForm(request.POST)
        if order_form.is_valid() and test_form.is_valid():
            new_order = order_form.save(commit=False)
            new_test = test_form.save(commit=False)

            # Process order form.
            new_order.company = order_form.cleaned_data['company']
            new_order.name = order_form.cleaned_data['name']
            new_order.name = order_form.cleaned_data['email']

            new_order.save()

            # Create and format job number into acceptable format.
            if len(str(new_order.id)) == 1:
                new_order.job_number = '17-000' + str(new_order.id)
            elif len(str(new_order.id)) == 2:
                new_order.job_number = '17-00' + str(new_order.id)
            elif len(str(new_order.id)) == 3:
                new_order.job_number = '17-0' + str(new_order.id)
            elif len(str(new_order.id)) == 4:
                new_order.job_number = '17-' + str(new_order.id)

            new_test.test_type = test_form.cleaned_data['test_type']
            new_test.air_flow_rate = test_form.cleaned_data['air_flow_rate']
            new_test.filter_description = test_form.cleaned_data['filter_description']

            new_order.save()
            #new_test.save()
        return HttpResponseRedirect(reverse('orders:form'))
    return render(request, 'orders/combined_form.html', {'order_form': order_form, 'test_form': test_form})