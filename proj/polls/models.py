from django.db import models


class Books(models.Model):
    author = models.CharField(max_length=100,verbose_name='Автор')
    name = models.CharField(max_length=100, verbose_name="Название книги")
    pub_date = models.DateField(auto_now=True,verbose_name="Дата публикации")
    count_pages = models.IntegerField()
# Create your models here.
