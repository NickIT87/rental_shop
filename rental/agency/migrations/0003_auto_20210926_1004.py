# Generated by Django 3.2.6 on 2021-09-26 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0002_advertising'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advertising',
            options={'ordering': ['created_at'], 'verbose_name': 'Рекламный банер', 'verbose_name_plural': 'Рекламные банеры'},
        ),
        migrations.AlterField(
            model_name='advertising',
            name='slogan',
            field=models.CharField(blank=True, max_length=40, verbose_name='Слоган'),
        ),
        migrations.AlterField(
            model_name='advertising',
            name='title',
            field=models.CharField(blank=True, max_length=40, verbose_name='Заголовок'),
        ),
    ]
