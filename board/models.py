from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name = "Заголовок")
    text = models.TextField(verbose_name = "Текст")
    email = models.EmailField(max_length=254, blank=False, verbose_name = "Email")
    published_date = models.DateTimeField(blank=True, null=True)
    premium = models.BooleanField(default=False)
    photo = models.ImageField(upload_to = 'photo/', height_field=None, width_field=None, max_length=100, blank=True, verbose_name = "Фото")
    city = models.CharField(max_length=100, verbose_name="Город", blank=True, )
    metro = models.CharField(max_length=100, verbose_name="Станция метро", blank=True)


    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title