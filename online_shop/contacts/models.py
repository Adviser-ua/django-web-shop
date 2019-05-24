from django.db import models

# Create your models here.


class Contact(models.Model):
    person = models.CharField(verbose_name='Контактное лицо', max_length=100)
    email = models.EmailField(verbose_name='Email', null=True)
    address = models.CharField(verbose_name='Адрес', max_length=250, null=True)
    instagram = models.CharField(verbose_name='Instagram', max_length=250, null=True)
    facebook = models.CharField(verbose_name='Facebook', max_length=250, null=True)
    m_phone = models.CharField(verbose_name='Номер телефона', max_length=30, null=True)

    def __str__(self):
        return 'Связь: {}'.format(self.person)
