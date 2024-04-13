# Generated by Django 4.2 on 2024-04-09 16:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='название товара')),
                ('price', models.PositiveIntegerField(verbose_name='цена товара')),
                ('description', models.TextField(verbose_name='описание товара')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='дата и время создания объявления')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='создатель объявления')),
            ],
            options={
                'verbose_name': 'объявление',
                'verbose_name_plural': 'объявления',
                'ordering': ['-created_at'],
            },
        ),
    ]
