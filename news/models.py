from django.db import models
    
class News(models.Model):
    title = models.CharField('Название', max_length=200)
    full_text = models.TextField('Статья')
    url = models.URLField('Видео')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новость"