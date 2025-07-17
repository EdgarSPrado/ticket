
from django.contrib import admin
from django.urls import path
from tickets.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ticket_home, name='ticket_home'),
    path('detalleticket/', detalle_ticket, name='detalleticket'),

]
