# Generated by Django 3.0.1 on 2023-07-22 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20230722_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_size',
        ),
        migrations.AddField(
            model_name='orderlineitem',
            name='product_metal',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
