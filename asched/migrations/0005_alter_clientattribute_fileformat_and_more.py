# Generated by Django 4.0.3 on 2022-07-07 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asched', '0004_alter_clientattribute_background_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientattribute',
            name='fileformat',
            field=models.CharField(choices=[('PDF', 'PDF'), ('TIFF', 'TIFF'), ('PNG', 'PNG')], max_length=20),
        ),
        migrations.AlterField(
            model_name='clientbasicinfo',
            name='cl_contact',
            field=models.IntegerField(default=''),
        ),
        migrations.AlterField(
            model_name='portraitshot',
            name='art',
            field=models.CharField(choices=[('anime style', 'anime style'), ('vector art', 'vector art'), ('pixel art', 'pixel art'), ('chibi style', 'chibi style')], max_length=20),
        ),
        migrations.AlterField(
            model_name='portraitshot',
            name='color',
            field=models.CharField(choices=[('black&white', 'black&white'), ('full color', 'full color'), ('sketch', 'sketch')], max_length=20),
        ),
        migrations.AlterField(
            model_name='portraitshot',
            name='shot',
            field=models.CharField(choices=[('wholebody', 'wholebody'), ('bust', 'bust'), ('headshot', 'headshot'), ('halfbody', 'halfbody')], max_length=20),
        ),
        migrations.AlterField(
            model_name='portraitshot',
            name='sizes',
            field=models.CharField(choices=[('2000 x 2000 px', '2000 x 2000 px'), ('3300 x 2550 px', '3300 x 2550 px'), ('4000 x 4000 px', '4000 x 4000 px')], max_length=20),
        ),
    ]