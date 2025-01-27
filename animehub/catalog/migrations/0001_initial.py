# Generated by Django 2.2.4 on 2019-08-27 16:26

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('russian', models.CharField(blank=True, max_length=128, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, unique=True)),
                ('filtered_name', models.CharField(blank=True, max_length=128, null=True)),
                ('real', models.BooleanField(default=True)),
                ('image', models.CharField(blank=True, max_length=400, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shikimori_id', models.PositiveIntegerField(unique=True)),
                ('title', models.CharField(max_length=400)),
                ('title_latin', models.CharField(blank=True, max_length=400, null=True)),
                ('slug', models.SlugField(blank=True, max_length=400)),
                ('description', models.TextField(blank=True, null=True)),
                ('score', models.CharField(blank=True, max_length=10, null=True)),
                ('kind', models.CharField(blank=True, max_length=10, null=True)),
                ('status', models.CharField(blank=True, max_length=20, null=True)),
                ('duration', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('episodes', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('episodes_aired', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('aired_on', models.DateField(blank=True, null=True)),
                ('released_on', models.DateField(blank=True, null=True)),
                ('rating', models.CharField(max_length=10)),
                ('english_titles', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), size=None)),
                ('japanese_titles', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), size=None)),
                ('other_titles', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=400), size=None)),
                ('next_episode_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('genres', models.ManyToManyField(to='catalog.Genre')),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.Image')),
                ('studios', models.ManyToManyField(to='catalog.Studio')),
            ],
        ),
    ]
