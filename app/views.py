from django.shortcuts import render

# Create your views here.
from .calculation import BMI_calculation
from rest_framework.views import APIView
import json
from .serailizer import  BMC_sera
from rest_framework.response import Response



class BmcView(APIView):
	def post(self,request):
		user_data=BMC_sera(data=request.data,many=True)
		user_data.is_valid(raise_exception=True)

		data=BMI_calculation(user_data.validated_data)
		nextdata=data.compute_and_csv()
		

		return Response({'Overweight counts':(nextdata[-2]=="Overweight").sum(),'data_file':request.META.get('HTTP_HOST','localhost:8000') +'/media/data.csv'})

