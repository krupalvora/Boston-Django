from django.shortcuts import redirect, render, HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from django.http import HttpResponse
from .models import Store
from moviepy.editor import *
from wsgiref.util import FileWrapper

def index(request):
    return render(request,'index.html')

def rotate_video(request,angle):
    try:
        video = VideoFileClip("./media/demo.mp4")
        rotated_clip = video.rotate(int(angle))
        rotated_clip.write_videofile("./media/demo_1.mp4", codec="libx264", audio_codec="aac")
        return redirect('/media/demo_1.mp4')
    except Exception as error:
        print(error)
        return HttpResponse("An Error occured")


def get_books(request):
    try:
        objects = Store.objects.all().values_list()
        return HttpResponse(objects)
    except Exception as error:
        print(error)
        return HttpResponse("An Error occured")

def get_book(request,book):
    try:
        objects = Store.objects.filter(book_id=book).all().values_list()
        return HttpResponse(objects)
    except Exception as error:
        print(error)
        return HttpResponse("An Error occured")

def add_book(request):
    try:
        if request.method == "POST":
            book = JSONParser().parse(request)
            print(book)
            save_book=Store(book_id=book["book_id"],author=book["author"],book_name=book["book_name"],price=book["price"])
            save_book.save()
            return JsonResponse(book)
    except Exception as error:
        print(error)
        return HttpResponse("An Error occured")
# {"book_id":"2","author":"Ravi kant","book_name":"rich dad","price":200}
    
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from .serializers import UserLoginSerializer
from django.contrib.auth import authenticate

class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserLoginView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            serializer = UserLoginSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.validated_data['username']
                password = serializer.validated_data['password']
                user = authenticate(request, username=user, password=password)
                if user:
                    token, created = Token.objects.get_or_create(user=user)
                    return Response({'token': token.key})
                else:
                    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
                print(error)
                return HttpResponse("An Error occured")