from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from web.models import CustomerProfile
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse, JsonResponse
# Emailing libraries
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.shortcuts import redirect
# Create your views here.
def home(request):
    return redirect('login')
@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    customer = CustomerProfile.objects.filter(customer=user)
    args = {'user': user, 'customer': customer}
    return render(request, 'profile.html', args)

@csrf_exempt
@login_required(login_url='/accounts/login/')
def order(request):
    if request.method == 'GET':
        user = request.user
        customer = CustomerProfile.objects.filter(customer=user)
        for i in customer:
            products = i.products.all()

        queryset = {'products': products, 'user': user, 'customer': customer}
        return render(request, 'order.html', queryset)
    else:
        user = request.user
        data = json.loads(request.body)
        print(data)
        print(data['order'])
        subject = 'J B RICHARDSON ORDER'
        sender = "orders@jbrichardson.co.uk"
        customer_email = data['email']
        recipient = ['bagheri.danial@gmail.com', customer_email]
        order = data['order']
        order = order.split('-')
        formatted_order = ""
        for i in order:
            formatted_order += i
            formatted_order += '\n'
        order_number = data['Order Number']
        delivery_date = data['Delivery Date']
        extra_info = data['Extra Info']
        message = """ 
        J B RICHARDSON BAKERY \n
        Thank you for placing your order with us. \n
        Customer Name: {} \n
        Your order:\n
        {} \n \n
        Order Purchase Number: {} \n
        Delivery Date: {} \n
        Extra information: \n
        {}
        """.format(user,formatted_order, order_number, delivery_date, extra_info)
        send_mail(subject, message, sender, recipient)
        # return HttpResponse("Got json data")
        return JsonResponse({'status':'ok'})
