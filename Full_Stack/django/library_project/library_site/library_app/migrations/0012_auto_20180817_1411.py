# Generated by Django 2.0 on 2018-08-17 21:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0011_auto_20180817_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='borrower',
            name='book',
        ),
        migrations.AddField(
            model_name='book',
            name='borrower',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='library_app.Borrower'),
        ),
    ]
