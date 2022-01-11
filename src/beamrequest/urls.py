from django.urls import include, path

from .views import (
    beam_request_home_page,
    beam_request_create_page,
    beam_request_detail_page,
    beam_request_update_page,
    beam_request_delete_page,
)

urlpatterns = [
   path('home/', beam_request_home_page, name='home'),
   path('create/', beam_request_create_page, name='create'),
   path('<str:project_code>/detail/', beam_request_detail_page, name='detail'),
   path('<str:project_code>/update/', beam_request_update_page, name='update'),
   path('<str:project_code>/delete/', beam_request_delete_page, name='delete'),
]