# Generated by Django 2.0 on 2018-08-15 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_book_checked_out'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='pub_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]
