from django.urls import path, include
from django.views.generic.base import RedirectView
from products import views
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    path('product-creation', staff_member_required(login_url='/accounts/login')
        (views.ProductCreate.as_view()), name='product-creation'),
    path('<slug:slug>', staff_member_required(login_url='/accounts/login')
        (views.ProductUpdate.as_view()), name='product-update'),
    # path('<slug:slug>/remove', staff_member_required(login_url='login')
    #     (views.ProductDelete.as_view()), name='product-delete'),
    ]
