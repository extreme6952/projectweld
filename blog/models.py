from trace import Trace
from django.db import models

from django.db.models import QuerySet

from django.utils import timezone

from django.urls import reverse


class PublishedManager(models.Manager):

    def get_queryset(self) -> QuerySet:
        return super().get_queryset().filter(status=Product.Status.PUBLISHED)



class Product(models.Model):

    class Status(models.TextChoices):

        DRAFT = 'DF','Draft'

        PUBLISHED = 'PB','Published'

    
    title = models.CharField(max_length=250)

    slug = models.SlugField(max_length=250)

    description = models.TextField()

    price = models.DecimalField(max_digits=10, decimal_places=2)

    publish = models.DateField(default=timezone.now)

    created = models.DateField(auto_now_add=True)

    updated = models.DateField(auto_now=True)

    status = models.CharField(max_length=2,
                              choices=Status.choices,
                              default=Status.DRAFT)
    
    objects = models.Manager()

    published = PublishedManager()


    class Meta:

        ordering = ['-publish']

        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self):

        return self.title

    
    def get_absolute_url(self):

        return reverse('welder:product_detail',args=[self.publish.year,
                                                     self.publish.month,
                                                     self.publish.day,
                                                     self.slug])
    


class Gallery(models.Model):

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='images')

    image = models.ImageField(upload_to='weldmedia/')








class Comment(models.Model):

    product = models.ForeignKey(Product,
                                on_delete=models.CASCADE,
                                related_name='comments')

    name = models.CharField(max_length=85)

    body = models.TextField()

    email = models.EmailField()

    created = models.DateField(auto_now_add=True)

    updated = models.DateField(auto_now=True)

    active = models.BooleanField(default=True)

    class Meta:

        ordering = ['created']

        indexes = [
            models.Index(fields=['created'])
        ]

    def __str__(self):
        
        return f"{self.name} by {self.product}"