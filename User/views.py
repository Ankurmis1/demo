from os import name

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from User.models import User
from User.serializer import UserSerializer


def home(request):
    return render(request,'first.html')

@api_view(['GET'])
def taskdetail(request):
    tasks=User.objects.all()
    serializer=UserSerializer(tasks,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def taskget(request,pk):
    tasks=User.objects.get(name=pk)
    serializer=UserSerializer(tasks,many=False)
    return Response(serializer.data)

@api_view(['POST'])
def taskpost(request):
    serializer=UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
