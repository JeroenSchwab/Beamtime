"""Beamtime URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from beamrequest.views import (
    beam_request_search_page,
    beam_request_create_page,
    beam_request_retrieve_page,
    beam_request_update_page,
    beam_request_delete_page,
    load_energys,
)

#from create.views import CreateReqView
#from create.views import CreateReq
#from create import views

urlpatterns = [
   path('searche/', beam_request_search_page, name='search'),
   path('create/', beam_request_create_page, name='create'),
   path('retrieve/', beam_request_retrieve_page, name='retrieve'),
   path('update/', beam_request_update_page, name='update'),
   path('delete/', beam_request_delete_page, name='delete'),
   path('admin/', admin.site.urls, name='admin'),
#	path('create/', CreateReqView.as_view(), name='create'),
#	path('create/', views.CreateReq_view, name='create'),

path('load-energys/', load_energys, name='load_energys'),

]
#from .views import (
#	main_page,
#	create_page,
#	update_page
#)

#urlpatterns = [
#    path('', main_page),
#    path('create/', create_page),
#    path('update/', update_page),
#    path('admin/', admin.site.urls),
#]
