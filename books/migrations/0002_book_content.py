# Generated by Django 4.2.3 on 2023-07-26 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.TextField(default='Test1'),
            preserve_default=False,
        ),
    ]
