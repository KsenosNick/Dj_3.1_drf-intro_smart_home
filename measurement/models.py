from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='Описание')

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='Датчик')
    temperature = models.DecimalField(max_digits=3, decimal_places=1, verbose_name='Температура')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата измерения')
    image = models.ImageField(null=True, verbose_name='Изображение', upload_to='uploads/%Y/%m/%d/', blank=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'