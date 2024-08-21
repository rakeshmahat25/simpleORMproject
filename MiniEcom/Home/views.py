from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Product
from .forms import CustomerForm, ProductForm


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer_list.html', {'customers': customers})


def customer_detail(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    products = customer.products.all()
    return render(request, 'customer_detail.html', {'customer': customer, 'products': products})


def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})


def add_product(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.customer = customer
            product.save()
            return redirect('customer_detail', customer_id=customer_id)
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form, 'customer': customer})


def edit_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer_list')
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'edit_customer.html', {'form': form, 'customer': customer})


def delete_customer(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    if request.method == 'POST':
        customer.delete()
        return redirect('customer_list')
    return render(request, 'confirm_delete.html', {'customer': customer})



