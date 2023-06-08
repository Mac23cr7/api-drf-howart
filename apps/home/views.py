from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

#Home Page
class HomePage(APIView):
    def get(self, request):
        return Response({"message": "OK"})