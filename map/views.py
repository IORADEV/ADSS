from django.shortcuts import render
from rest_framework import status, exceptions
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,  get_authorization_header
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework import authentication
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, get_user_model
from django.core.exceptions import ObjectDoesNotExist

from user_management.models import ExtendedUser
from .models import TvmRange4326, TvmDivision

from .serializers import TvmRangeSerializers, TmvDivisionSerializers


class MapView(APIView):
    
    def get(self, request):
        title = "DSS 2.0"
        if request.user.is_authenticated:
            # redirect(to=reverse('map'))
            qs_division = TvmDivision.objects.all()
            qs_range = TvmRange4326.objects.all()
            context = {'title': title, 'division': qs_division, 'range': qs_range}
            print("Logged in")
        else:
            print("Not logged in")

        return render(request, 'map.html', context)


class ResultView(APIView):

    def get(self, response):
        title = "DSS 2.0"
        return render(response, 'result.html', {'title': title})


class TmvRangeView(APIView):

    def get(self, request):

        qs = TvmRange4326.objects.all()
        #serializer = TvmRangeSerializers(qs, many=True)

        #print(qs.name)
        return render(request, 'division_dropdown_list.html', {'division': qs})


class TmvDivisionView(APIView):

    def get(self, response):

        qs = TvmDivision.objects.all()
        serializer = TmvDivisionSerializers(qs, many=True)

        return Response(serializer.data)
