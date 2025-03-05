# Generated by Django 5.1.6 on 2025-03-05 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itstepproject', '0002_alter_job_company'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('description', models.TextField()),
                ('company', models.CharField(max_length=100, verbose_name='Название компании')),
                ('location', models.CharField(max_length=100, verbose_name='Место работы')),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
