# Generated by Django 3.1.1 on 2020-09-11 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='category', to='collection.Collection'),
        ),
    ]
