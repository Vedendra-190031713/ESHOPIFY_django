# Generated by Django 3.1.7 on 2021-05-16 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0012_auto_20210514_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='related_product_category',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]