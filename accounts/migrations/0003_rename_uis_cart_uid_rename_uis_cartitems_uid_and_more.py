# Generated by Django 4.1.6 on 2023-03-21 10:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_cart_cartitems'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cart',
            old_name='uis',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='cartitems',
            old_name='uis',
            new_name='uid',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='uis',
            new_name='uid',
        ),
    ]
