# Generated by Django 2.0 on 2018-08-17 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0007_auto_20180817_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrower',
            name='checkout_in',
        ),
        migrations.RemoveField(
            model_name='borrower',
            name='checkout_time',
        ),
        migrations.AddField(
            model_name='book',
            name='checkin_time',
            field=models.DateTimeField(auto_now_add=True, default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='checkout_time',
            field=models.DateTimeField(null=True),
        ),
    ]