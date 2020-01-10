from django.shortcuts import render
from rest_framework import status, exceptions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,  get_authorization_header
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import authentication
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ObjectDoesNotExist

from .models import ExtendedUser
# Create your views here.


class LandingPage(APIView):

    def get(self, request):
        title = "DSS 2.0"
        return render(request, 'index.html', {'title': title})


class RegisterartionPage(APIView):

    def get(self, request):
        title = "DSS 2.0"
        return render(request, 'registeration.html', {'title': title})

'''
View class to create account
Http POST operations only
Return Success message, Provided contact number not already registered
'''


class SignupList(APIView):

    def post(self, request, *args, **kwargs):

        print(request.data)
        if not request.data:
            return Response({"Error": "Please provide all fields"}, status=status.HTTP_204_NO_CONTENT)

        username = request.data.get('username', None)
        password = request.data.get('password', None)
        email = request.data.get('email', '')
        phone = request.data.get('phone', None)

        # print(phone_check)

        try:

            username_check = ExtendedUser.objects.get(username=username)
            #print(username_check)
            if username_check:
                return Response({"Error": "Username already exist", "status": 1})
        except ObjectDoesNotExist:

            try:
                user = ExtendedUser(
                    username=username,
                    email=email,
                    phone=phone,
                    password=password
                )

                user.set_password(password)
                user.save()


            except:
                return Response({"Error": "Username already exists"})

        return Response({'User Created'})


'''
View class to Login
Http POST operations only
Returns JWT Token for Authentication
'''


class LoginList(APIView):

    def post(self, request):

        # if not request.data:

        # return Response({"Error": "Please provide username and password"}, status=status.HTTP_204_NO_CONTENT)

        username = request.data.get('username', None)
        password = request.data.get('password', None)

        print(username)
        if authenticate(username=username, password=password):
            user = ExtendedUser.objects.get(username=username)

            return Response({'id': user.id})

        else:
            return Response({"Error": "Invalid login  details"})

        return Response(jwt_token)
