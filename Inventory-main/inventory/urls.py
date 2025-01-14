from django.urls import path, include

from inventory import views

urlpatterns = [
    path('product-bulk-create-update/', views.ProductView.as_view(), name='product-bulk-create-update'),
    path('host-bulk-create-update/', views.HostView.as_view(), name='host-bulk-create-update')
]
