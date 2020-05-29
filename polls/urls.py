from django.urls import path
from .views import polls_details, polls_list


urlpatterns = [

    path('polls', polls_list, name='poll_list'),
    path('polls/<int:pk>', polls_details, name='polls_detail')

]