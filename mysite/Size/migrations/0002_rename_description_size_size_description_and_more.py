# Generated by Django 4.0.4 on 2022-06-30 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Size', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='size',
            old_name='description',
            new_name='size_description',
        ),
        migrations.RenameField(
            model_name='size',
            old_name='name',
            new_name='size_name',
        ),
        migrations.AddField(
            model_name='size',
            name='isactive',
            field=models.BooleanField(default=True),
        ),
    ]
