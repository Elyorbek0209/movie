# Generated by Django 3.0.6 on 2020-05-31 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieReview', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieinfo',
            old_name='movie_genere',
            new_name='movie_type',
        ),
        migrations.AddField(
            model_name='movieinfo',
            name='movie_release_date',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
    ]
