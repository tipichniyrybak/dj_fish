from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.conf import settings

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.FileField(upload_to='static/img/profile')

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class FishingPlace(models.Model):
    name = models.CharField('Name of place', max_length=100)
    lant = models.DecimalField('Lant of place', max_digits=10, decimal_places=8)
    long = models.DecimalField('Long of place', max_digits=10, decimal_places=8)
    description = models.TextField('Description of place')
    photos = models.CharField('Photos of place' , max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рыболовное место'
        verbose_name_plural = 'Рыболовные места'

    def save(self, *args, **kwargs):
        if FishingPlace.objects.filter(name=self.name).exists():
            print('Place name already exists!')
            return 0
        else:
            super(FishingPlace, self).save(*args, **kwargs)
            # return FishingPlace.objects.filter(name=self.name).values('id')
            return self.id


class Order(models.Model):
    fishing_place = models.ForeignKey(FishingPlace, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    description = models.TextField('Description of order')
    photos = models.CharField('Photos of order', max_length=300)

    def __str__(self):
        return self.user_id

    class Meta:
        verbose_name = 'Отчет о рыбалке'
        verbose_name_plural = 'Отчеты о рыбалке'
