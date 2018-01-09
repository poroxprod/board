from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    email = models.EmailField(max_length=254, blank=True)
    published_date = models.DateTimeField(blank=True, null=True)
    premium = models.BooleanField(default=False)
    photo = models.ImageField(upload_to = 'media/', default = 'media/no-img.jpg', height_field=None, width_field=None, max_length=100)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title