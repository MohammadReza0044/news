from django.db import models

class News(models.Model):
    news_id = models.CharField(max_length=100) 
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.CharField(max_length=255)
  

    def __str__(self):
        return self.title