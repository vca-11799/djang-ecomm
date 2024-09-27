# Generated by Django 5.0.6 on 2024-07-07 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_remove_orderproduct_color_remove_orderproduct_size_and_more'),
        ('store', '0003_rename_variations_variation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='variation',
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='variations',
            field=models.ManyToManyField(blank=True, to='store.variation'),
        ),
    ]
