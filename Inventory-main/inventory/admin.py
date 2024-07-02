from django.contrib import admin

from inventory.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price", "type", "visible", "discount")
    list_filter = ("type", "visible")
    list_editable = ("price", "visible", "discount")

@admin.register(Host)
class HostAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Host._meta.fields]
    history_list_display = ['cmdbid','name','product','manufacturer','site','area','status','usage_type','urgency','primary_function','monitored','sox_relevance','dns','domain','ip_address','owner','modified_at','modified_by']
    search_fields = ['name','cmdbid','product','manufacturer','site','area','status','usage_type','urgency','primary_function','monitored','sox_relevance','dns','domain','ip_address','owner','modified_by','last_seen']
    list_filter = ['product','manufacturer','site','area','status','usage_type','urgency','primary_function','monitored','sox_relevance','domain']