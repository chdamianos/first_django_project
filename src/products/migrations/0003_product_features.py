# Generated by Django 2.1.5 on 2020-11-29 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20201129_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='features',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
