# Generated by Django 2.0 on 2018-08-17 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0010_auto_20180817_1153'),
    ]

    operations = [
        migrations.RenameField(
            model_name='borrower',
            old_name='books',
            new_name='book',
        ),
    ]
