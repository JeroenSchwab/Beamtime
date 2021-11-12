from django.urls import include, path

from .views import (
   summary_home_page,
   summary_chart_data,
   pie_chart,
   bar_chart,
)

urlpatterns = [
   path('home/', summary_home_page, name='home'),
   path('home/data/', summary_chart_data, name='summary_chart_data'),
   path('pie-chart/', pie_chart, name='pie-chart'),
   path('bar-chart/', bar_chart, name='bar-chart'),
#   path('create/', beam_request_create_page, name='create'),
#   path('<str:Project_Code>/detail/', beam_request_detail_page, name='detail'),
#   path('<str:Project_Code>/update/', beam_request_update_page, name='update'),
#   path('<str:Project_Code>/delete/', beam_request_delete_page, name='delete'),
]