# Generated by Django 4.1.5 on 2023-06-01 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodz', '0003_fb'),
    ]

    operations = [
        migrations.CreateModel(
            name='foodlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=100)),
                ('pat', models.CharField(max_length=100)),
                ('dec', models.CharField(max_length=100)),
            ],
        ),
    ]
