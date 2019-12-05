from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import Order
from .forms import OrderForm


def orders_list(request):
    orders = Order.objects.all()
    return render(request, 'order/order_list.html', {'orders': orders})


def order_detail(request, number):
    try:
        order = Order.objects.get(number=number)
    except Order.DoesNotExist:
        raise Http404(f"Заказ {number} не существует.")

    if request.method == "POST":
        order_form = OrderForm(request.POST, instance=order)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()
        return redirect("orders_list")
    else:
        order_form = OrderForm(instance=order)
        return render(request, 'order/order_detail.html', {'order_form': order_form})



def order_new(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            order.save()
    else:
        order_form = OrderForm()
    return render(request, 'order/order_detail.html', {'order_form': order_form})
