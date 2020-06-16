from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'category' 
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

class News(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news' 
    
    def __str__(self):
        return self.title


