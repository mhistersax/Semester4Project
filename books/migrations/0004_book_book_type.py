# Generated by Django 5.0.4 on 2024-05-09 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_book_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_type',
            field=models.CharField(choices=[('book', 'Book'), ('video', 'Video')], default='book', max_length=5),
        ),
    ]
