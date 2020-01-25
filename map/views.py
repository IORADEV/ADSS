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

from user_management.models import ExtendedUser
from .models import TvmRange4326

from .serializers import TvmRangeSerializers


class MapView(APIView):
    
    def get(self, request):

        if request.user.is_authenticated:
            # redirect(to=reverse('map'))
            print("Logged in")
        else:
            print("Not logged in")
        title = "DSS 2.0"
        return render(request, 'map.html', {'title': title})


class ResultView(APIView):

    def get(self, response):
        title = "DSS 2.0"
        return render(response, 'result.html', {'title': title})


class TmvRangeView(APIView):

    def get(self, response):
        print("start")
        queryset = TvmRange4326.objects.all()
        print(queryset)
        #print(query)
        print("end")
        serializer = TvmRangeSerializers(queryset)
        print(serializer.data)
        return Response(serializer.data)
