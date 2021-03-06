from django.urls import include, path

from .views import (
   hours_create_page,
   hours_home_page,
   hours_update_page,
    #hours_delete_page,
)

urlpatterns = [
   path('home/', hours_home_page, name='home'),
   path('create/', hours_create_page, name='create'),
   #path('<str:Project_Code>/detail/', hours_detail_page, name='detail'),
   path('update/', hours_update_page, name='update'),
   #path('<str:Project_Code>/delete/', hours_delete_page, name='delete'),
]