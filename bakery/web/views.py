from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from web.models import CustomerProfile


# Create your views here.
@login_required(login_url='/account/login/')
def profile(request):
    user = request.user
    customer = CustomerProfile.objects.filter(customer=user)
    args = {'user': user, 'customer': customer}
    return render(request, 'profile.html', args)


@login_required(login_url='/account/login/')
def order(request):
    user = request.user
    customer = CustomerProfile.objects.filter(customer=user)
    for i in customer:
        products = i.products.all()

    queryset = {'products': products}
    return render(request, 'order.html', queryset)
