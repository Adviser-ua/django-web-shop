# Generated by Django 2.2 on 2019-05-29 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='contact_number',
            field=models.CharField(default='', max_length=25, verbose_name='Номер телефона'),
        ),
    ]
