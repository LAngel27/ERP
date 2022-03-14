from django.http import HttpResponse, request
from django.shortcuts import render


def sale_home(request):
    return HttpResponse('sale order!!!!!"')


def list_view_sales(request):
    return render(request, 'sale/list_view.html',{'title': 'Hello word!!'})