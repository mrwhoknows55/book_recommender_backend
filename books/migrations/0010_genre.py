# Generated by Django 3.2.4 on 2021-08-09 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_alter_book_isbn13'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.TextField(max_length=50, unique=True)),
            ],
        ),
    ]
