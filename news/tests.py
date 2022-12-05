from django.test import TestCase
from .models import News

class NewsModelTest(TestCase):
    
    def setUp(self):
        News.objects.create(
           news_id =  111,
           title = 'test',
           content = 'test',
           image = 'test'
        )

    def test_title_content(self):
        news = News.objects.get(id=1)
        excepted_object_name = f'{news.title}'
        self.assertEqual(excepted_object_name , 'test')