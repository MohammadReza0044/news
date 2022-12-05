from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

from .models import News
from . serializers import NewsSerializer


def news_get(request):
    response = requests.get('https://feeds.npr.org/1004/feed.json').json()
    for r in response['items']:
        r['id']
        r['title']
        r['content_html']
        r['image']
        new_news = News.objects.get_or_create(news_id=r['id'], title = r['title'], content=r['content_html'], image=r['image'])

    return HttpResponse ('ok')


class News_List (APIView):
    def get (self,request):
        news_get(request)
        news = News.objects.all() [0:5]
        serializer = NewsSerializer (news, many = True)
        return Response (serializer.data) 



    
