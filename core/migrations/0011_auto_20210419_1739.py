# Generated by Django 3.1.7 on 2021-04-19 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_item_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
