# Generated by Django 5.0.4 on 2024-05-12 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_remove_book_video_book_movie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='book_type',
            field=models.CharField(blank=True, choices=[('', 'Please select book type'), ('book', 'Book'), ('video', 'Video')], default='', max_length=5),
        ),
    ]