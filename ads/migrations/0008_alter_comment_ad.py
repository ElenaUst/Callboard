# Generated by Django 4.2 on 2024-04-13 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0007_ad_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='ad',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comment_ad', to='ads.ad', verbose_name='объявление, под которым оставлен отзыв'),
        ),
    ]
