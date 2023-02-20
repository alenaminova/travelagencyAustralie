from django.shortcuts import render
from django.http import JsonResponse, HttpRequest, HttpResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.parsers import JSONParser
from rest_framework import generics
from rest_framework import mixins

from viewer.models import travel_agency_Australie

from api.serializers import travel_agency_AustralieSerializer

# Create your views here
"""
class travel_agency_Australie (viewsets.ModelViewSet):
    queryset = .objects.all()
    serializer_class = travel_agency_AustralieSerializer
    permission_classes = [permissions.IsAuthenticated]
"""""

class travel_agency_Australie(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = travel_agency_Australie.objects.all()
    serializer_class = travel_agency_AustralieSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class travel_agency_Australie (mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
            generics.GenericAPIView):
    queryset = travel_agency_Australie.objects.all()
    serializer_class = travel_agency_AustralieSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)