from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login/')
def profile(request):
    args = {'user': request.user}
    return render(request, 'profile.html', args)
