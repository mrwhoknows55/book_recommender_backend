# Generated by Django 3.2.4 on 2021-06-29 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_alter_book_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='avg_rating',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]