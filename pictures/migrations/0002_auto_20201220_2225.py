# Generated by Django 3.1.4 on 2020-12-20 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='name',
            new_name='photographer',
        ),
    ]
