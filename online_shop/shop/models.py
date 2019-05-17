import sys

from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from PIL import Image
from io import BytesIO
# Create your models here.


# Модель продукта
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d/', blank=True, verbose_name="Изображение товара")
    img = models.ImageField(blank=True, verbose_name="превью")
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="На складе")

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])

    # def save(self):
    #     # Opening the uploaded image
    #     im = Image.open(self.img)
    #
    #     output = BytesIO()
    #
    #     # Resize/modify the image
    #     im = im.resize((100, 100))
    #
    #     # after modifications, save it to the output
    #     im.save(output, format='JPEG', quality=100)
    #     output.seek(0)
    #
    #     # change the imagefield value to be the newley modifed image value
    #     self.img = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.img.name.split('.')[0], 'image/jpeg',
    #                                     sys.getsizeof(output), None)
    #
    #     super(Product, self).save()

    def save(self, **kwargs):
        print(kwargs.items())
        im = Image.open(self.image)
        output = BytesIO()
        im = im.resize((100, 100))
        im.save(output, format='JPEG', quality=100)
        output.seek(0)
        self.img = InMemoryUploadedFile(output, 'ImageField', "%s.jpg" % self.img.name.split('.')[0], 'image/jpeg',
                                            sys.getsizeof(output), None)
        super(Product, self).save(kwargs)