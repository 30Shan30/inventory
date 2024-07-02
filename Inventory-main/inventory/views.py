from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from inventory import models, serializers
from inventory.models import *
from inventory.serializers import *

def validate_ids(data, field="cmdbid", unique=True):

    if isinstance(data, list):
        id_list = [(x[field]) for x in data]

        if unique and len(id_list) != len(set(id_list)):
            raise ValidationError("Multiple updates to a single {} found".format(field))

        return id_list

    return [data]


class ProductView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer

    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True
        return super(ProductView, self).get_serializer(*args, **kwargs)

    def get_queryset(self, ids=None):
        if ids :
            queryset = Product.objects.filter(id__in=ids)
        else:
            queryset = Product.objects.all()
        return queryset

    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):

        ids = validate_ids(request.data)

        instances = self.get_queryset(ids=ids)

        serializer = self.get_serializer(
            instances, data=request.data, partial=False, many=True
        )

        serializer.is_valid(raise_exception=True)

        self.perform_update(serializer)

        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()


class HostView(generics.ListCreateAPIView):
    #queryset = Host.objects.all().select_related() 
    #http_method_names = '__all__'
    #queryset = Host.objects.none()
    serializer_class = HostSerializer
    def get_serializer(self, *args, **kwargs):
        if isinstance(kwargs.get("data", {}), list):
            kwargs["many"] = True
        return super(HostView, self).get_serializer(*args, **kwargs)

    def get_queryset(self, ids=None):
        if ids:
            queryset = Host.objects.filter(id__in=ids)
        else:
            queryset = Host.objects.all()
        return queryset

    def update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        ids = validate_ids(request.data)
        instances = self.get_queryset(ids=ids)
        serializer = self.get_serializer(
            instances, data=request.data, partial=False, many=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def perform_update(self, serializer):
        serializer.save()