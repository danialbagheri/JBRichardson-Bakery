from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from web.models import CustomerProfile, Order
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
        order_model = Order(customer=user,po_number=order_number,delivery_date=delivery_date,order_detail=formatted_order,extra_information=extra_info)
        tracking_number=str(order_model.tracking_number)
        order_model.save()
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
        url = '/accounts/order/successful/?resp=%s'%tracking_number
        return JsonResponse({'status':'ok','url': url})
        # return redirect(url)

def successful(request):
    resp = request.GET.get('resp')
    print(request.GET.get('resp'))
    return render(request, 'successful_order.html',{'tracking':resp})