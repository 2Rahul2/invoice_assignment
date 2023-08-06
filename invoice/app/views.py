from django.shortcuts import render ,redirect
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Invoice ,InvoiceDetail
from .serializers import InvoiceSerializer ,InvoiceDetailSerializer
    
def homePage(request):
    return render(request , 'app/index.html')
def invoiceForm(request):
    return render(request ,'app/invoice.html')
@api_view(['POST'])
def getInvoiceData(request):
    InvoiceObject = Invoice.objects.get(invoice_no = request.data['invoiceNo'])
    data = {
        'invoice':InvoiceObject,
        'description':request.data['description'],
        'quantity':request.data['quantity'],
        'unit_price':request.data['unit_price'],
        'price':request.data['price'],
    }
    print(data)
    invoiceDetailObject = InvoiceDetail.objects.create(**data)
    invoiceDetailObject.save()
    InvoiceDetailsSerializerObject = InvoiceDetailSerializer(invoiceDetailObject)
    return Response(InvoiceDetailsSerializerObject.data)
