# Generated by Django 3.2.7 on 2022-10-31 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_alter_movie_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField(max_length=500)),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='movies.movie')),
            ],
        ),
    ]
