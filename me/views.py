from django.shortcuts import render
from django.shortcuts import HttpResponse
from .serialize import testingser
from base.models import test
from rest_framework import status
from django.views import View
from rest_framework.views import APIView
# Create your views here.
from rest_framework.response import Response
class temp(View):
    
    def get(self,request):
        
        if request.method=='POST':
            val=request.POST['name']
            print(val)
        
        return render(request,'base/new.html')
class working(View):

    def work(request):
        return HttpResponse("hello mowa")
            



class testing(APIView):
    def get(self,request):
        val=test.objects.all()
        print(val)
        ser=testingser(val,many=True)
        return Response(ser.data)
class teste(APIView):

    def post(self,request):
        # val=test.objects.get(id=pk)
        ser=testingser(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
        
class puter(APIView):
    def put(self,request,pk):
        val=test.objects.get(id=pk)
        print(val)
        ser=testingser(val,data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

class patcher(APIView):
    def patch(self,request,pk):
        val=test.objects.get(id=pk)
        ser=testingser(val,data=request.data,partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data,status=status.HTTP_201_CREATED)
        return Response(ser.errors)