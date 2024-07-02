from django.db import models
from django.core.validators import RegexValidator
#from simple_history.models import HistoricalRecords

class Product(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    price = models.IntegerField()
    type = models.CharField(max_length=255)
    visible = models.BooleanField(default=False)
    discount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title
    
class Host(models.Model):
    cmdbid            = models.CharField(primary_key=True, max_length=15, validators=[RegexValidator('^CMDB[0-9]{11}','invalid CMDB ID')])
    name              = models.CharField(max_length=100) ## by default blank=False, null=False
    product           = models.CharField(max_length=150, null=True)###models.CharField(max_length=50, choices=PRODUCT_CHOICES) #product           = models.CharField(max_length=50, choices=PRODUCT_CHOICES)
    manufacturer      = models.CharField(max_length=50, null=True)
    site              = models.CharField(max_length=50, null=True)
    area              = models.CharField(max_length=50, null=True)
    status            = models.CharField(max_length=30, null=True)
    usage_type        = models.CharField(max_length=30, null=True)
    urgency           = models.CharField(max_length=30, null=True)
    primary_function  = models.CharField(max_length=30, null=True)
    monitored         = models.CharField(max_length=30, null=True)
    sox_relevance     = models.CharField(max_length=50, null=True)
    dns               = models.CharField(max_length=30, null=True)
    domain            = models.CharField(max_length=30, null=True)
    ip_address        = models.GenericIPAddressField(null=True)
    owner             = models.CharField(max_length=11, validators=[RegexValidator('^IF[0-9]{8}','invalid Global ID')],null=True)
    last_seen         = models.DateTimeField(null=True)  
    modified_at       = models.DateTimeField()
    modified_by       = models.CharField(max_length=50)
    #history = HistoricalRecords()

    def __str__(self):
        return self.cmdbid
    
    class Meta:
        db_table = "repo_host"