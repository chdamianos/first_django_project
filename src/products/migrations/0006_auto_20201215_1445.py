# Generated by Django 2.1.5 on 2020-12-15 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20201129_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='features',
            field=models.BooleanField(default=True),
        ),
    ]
