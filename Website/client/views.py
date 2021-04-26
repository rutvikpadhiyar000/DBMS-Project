from django.shortcuts import render, redirect
from django.http import HttpResponse
from work.models import clean_request
from django.utils import timezone

# Create your views here.
placed = False
def home(request):
    global placed
    return render(request, 'index.html', {'placed': placed})

def create_order(address):
    order = clean_request(receive_date=timezone.now(), address=address)
    global placed
    placed = True
    return redirect('home')

def place_request(request):
    global placed
    placed = False
    address = request.POST["address"]
    return create_order(address=address)