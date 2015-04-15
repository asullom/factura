from django.shortcuts import render
from rest_framework import serializers, viewsets, permissions
from oauth2_provider.ext.rest_framework import TokenHasReadWriteScope, \
    TokenHasScope

from .models import Cliente
# Create your views here.

#from django.utils.decorators import method_decorator
#from django.views.decorators.csrf import csrf_exempt


class ClienteSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Cliente


class ClienteViewSet(viewsets.ModelViewSet):

    permission_classes = [permissions.IsAuthenticated]
    #required_scopes = ['groups']
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

"""
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(ClienteViewSet, self).dispatch(*args, **kwargs)
"""
