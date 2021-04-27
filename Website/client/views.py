from django.shortcuts import render, redirect
from django.http import HttpResponse
from work.models import clean_request
from django.utils import timezone
from .models import client

# Create your views here.
placed = False
def home(request):
    global placed
    return render(request, 'index.html', {'placed': placed})

def create_order(client):
    order = clean_request.objects.create(receive_date=timezone.now(), client=client, address=client.client_address)
    global placed
    placed = True
    return redirect('home')

def place_request(request):
    global placed
    placed = False
    address = request.GET["address"]
    contact = request.GET["contact"]
    name = request.GET["name"]
    cli = client.objects.create(client_address=address, client_name=name, client_contact=contact)
    return create_order(cli)