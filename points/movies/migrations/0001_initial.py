# Generated by Django 5.0.4 on 2024-05-09 22:15

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('book_category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('publication_date', models.DateField()),
                ('isbn', models.CharField(max_length=20, unique=True)),
                ('description', models.TextField(blank=True)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('downloadable', models.BooleanField(default=False)),
                ('book_type', models.CharField(choices=[('book', 'Book'), ('video', 'Video')], default='book', max_length=5)),
                ('image', models.ImageField(blank=True, null=True, upload_to='book_images', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('video', models.FileField(blank=True, null=True, upload_to='book_videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4', 'avi', 'mkv'])])),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='book_category.bookcategory')),
            ],
        ),
    ]