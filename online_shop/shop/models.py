from django.db import models
from django.conf import settings

# Модель продукта
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")

    class Meta:
        ordering = ['name']
        index_together = [
            ['id']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id])

    # def save(self, **kwargs):
    #     print(kwargs.items())
    #     im = Image.open(self.image)
    #     output = BytesIO()
    #     im = im.resize((100, 100))
    #     im.save(output, format='JPEG', quality=100)
    #     output.seek(0)
    #     self.img = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.img.name.split('.')[0], 'image/jpeg',
    #                                     sys.getsizeof(output), None)
    #     super(Product, self).save(kwargs)


class ProductImages(models.Model):
    property = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=settings.MEDIA_DIR + 'product/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
