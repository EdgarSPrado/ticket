from django.shortcuts import render

def ticket_home(request):
    return render(request, 'home.html')

def detalle_ticket(request):
    return render(request, 'detalleticket.html')