# Generated by Django 5.0.3 on 2024-04-24 14:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('carts', '0002_cartitem_variations'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='date_aded',
            new_name='date_added',
        ),
    ]