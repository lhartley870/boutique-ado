# Generated by Django 3.2 on 2022-04-08 13:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0005_order_order_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='order_profile',
            new_name='user_profile',
        ),
    ]
