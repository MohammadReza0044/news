from django.urls import path 
from .views import News_List

urlpatterns = [
    path('', News_List.as_view()),

]