from django.shortcuts import render

# Create your views here.
from rest_framework . response import Response
from . models import Product
from . serializers import ProducSerializer
from rest_framework.decorators import api_view



@api_view(['GET'])
def product_list(request):

    if request.method == 'GET':

        # get all of the products / Get a list of all the products

        products = Product.objects.all()

        serializer = ProducSerializer(products, many = True) #serialize our products into Json based format

        return Response(serializer.data)





