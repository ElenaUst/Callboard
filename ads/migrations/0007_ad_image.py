# Generated by Django 4.2 on 2024-04-12 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_alter_comment_ad'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ads/', verbose_name='фото товара'),
        ),
    ]
