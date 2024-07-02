from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from inventory import models
from inventory.models import *

class ProductBulkCreateUpdateSerializer(serializers.ListSerializer):
    def create(self, validated_data):
        product_data = [Product(**item) for item in validated_data]
        return Product.objects.bulk_create(product_data)

    def update(self, instance, validated_data):
        instance_hash = {index: i for index, i in enumerate(instance)}
        result = [
            self.child.update(instance_hash[index], attrs)
            for index, attrs in enumerate(validated_data)
        ]
        writable_fields = [
            x
            for x in self.child.Meta.fields
            if x not in self.child.Meta.read_only_fields
        ]

        try:
            self.child.Meta.model.objects.bulk_update(result, writable_fields)
        except IntegrityError as e:
            raise ValidationError(e)

        return result


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["id", "title", "description", "price", "type", "visible", "discount", "created_at", "updated_at"]
        read_only_fields = ['id', ]
        list_serializer_class = ProductBulkCreateUpdateSerializer

class HostBulkCreateUpdateSerializer(serializers.ListSerializer):
    def create(self, validated_data):  
        host_data = [Host(**item) for item in validated_data]  
        return Host.objects.bulk_create(host_data)
    # def update(self, instance, validated_data):
    #     # Maps for id->instance and id->data item.
    #     host_mapping = {Host.id: Host for Host in instance}
    #     data_mapping = {item['cmdbid']: item for item in validated_data}

    #     # Perform creations and updates.
    #     ret = []
    #     for host_id, data in data_mapping.items():
    #         host = host_mapping.get(host_id, None)
    #         if host is None:
    #             ret.append(self.child.create(data))
    #         else:
    #             ret.append(self.child.update(host, data))

    #     # Perform deletions.
    #     for host_id, host in host_mapping.items():
    #         if host_id not in data_mapping:
    #             host.delete()

    #     return ret
    def update(self, instance, validated_data):
        instance_hash = {index: i for index, i in enumerate(instance)}
        result = [
            self.child.update(instance_hash[index], attrs)
            for index, attrs in enumerate(validated_data)
        ]
        writable_fields = [
            x
            for x in self.child.Meta.fields
            if x not in self.child.Meta.read_only_fields
        ]

        try:
            self.child.Meta.model.objects.bulk_update(result, writable_fields)
        except IntegrityError as e:
            raise ValidationError(e)

        return result

class HostSerializer(serializers.ModelSerializer):  

    class Meta:  
        model = Host  
        fields = ['cmdbid','name','product','manufacturer','site','area','status','usage_type','urgency','primary_function','monitored','sox_relevance','dns','domain','ip_address','owner','last_seen','modified_at','modified_by']
        #read_only_fields = ['cmdbid',]  
        list_serializer_class = HostBulkCreateUpdateSerializer