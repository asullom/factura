from django.shortcuts import render
from rest_framework import serializers, viewsets

from .models import Cliente
# Create your views here.

#from django.utils.decorators import method_decorator
#from django.views.decorators.csrf import csrf_exempt


class ClienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cliente


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

"""
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ClienteViewSet, self).dispatch(*args, **kwargs)
"""
