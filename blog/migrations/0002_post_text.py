# Generated by Django 3.2.2 on 2021-05-12 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default='Test'),
            preserve_default=False,
        ),
    ]