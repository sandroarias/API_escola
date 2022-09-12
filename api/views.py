from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EscolaSerializer
from .models import Escola


class EscolaViewset(viewsets.ModelViewSet):
    queryset = Escola.objects.all()
    serializer_class = EscolaSerializer
