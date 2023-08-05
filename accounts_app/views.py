from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def accounts(request, username):
    return render(request, "accounts_app/profile.html")
