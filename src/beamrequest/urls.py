from django.urls import include, path

from .views import (
    beam_request_search_page,
    beam_request_create_page,
    beam_request_detail_page,
    beam_request_update_page,
    beam_request_delete_page,
    load_energys,
)

urlpatterns = [
   path('search/', beam_request_search_page, name='search'),
   path('create/', beam_request_create_page, name='create'),
   path('detail/', beam_request_detail_page, name='detail'),
   path('update/', beam_request_update_page, name='update'),
   path('delete/', beam_request_delete_page, name='delete'),
   path('load-energys/', load_energys, name='load_energys'),
]