# Generated by Django 3.0.6 on 2020-05-31 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MovieInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=100)),
                ('movie_review', models.CharField(max_length=3)),
                ('movie_genere', models.CharField(max_length=50)),
            ],
        ),
    ]
