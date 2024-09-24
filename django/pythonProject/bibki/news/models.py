from django.db import models

# Create your models here.
class Articles(models.Model):
    title = models.CharField('Название', max_length=150, default='Добавьте новость и получите +15') # Название новости, до 150 симв
    anonce = models.CharField('Анонс', max_length=250, default='Добавьте аннотацию к новости') # Аннотация, макс 250 симв
    full_text = models.TextField('Здесь будет к примеру статья')
    date = models.DateTimeField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'