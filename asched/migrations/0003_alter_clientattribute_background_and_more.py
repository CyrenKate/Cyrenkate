# Generated by Django 4.0.3 on 2022-07-07 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asched', '0002_clientattribute_clientbasicinfo_portraitshot_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientattribute',
            name='background',
            field=models.CharField(choices=[('transparent', 'transparent'), ('simple', 'simple')], max_length=20),
        ),
        migrations.AlterField(
            model_name='clientattribute',
            name='fileformat',
            field=models.CharField(choices=[('PDF', 'PDF'), ('PNG', 'PNG'), ('TIFF', 'TIFF')], max_length=20),
        ),
        migrations.AlterField(
            model_name='portraitshot',
            name='art',
            field=models.CharField(choices=[('vector art', 'vector art'), ('anime style', 'anime style'), ('chibi style', 'chibi style'), ('pixel art', 'pixel art')], max_length=20),
        ),
        migrations.AlterField(
            model_name='portraitshot',
            name='color',
            field=models.CharField(choices=[('black&white', 'black&white'), ('sketch', 'sketch'), ('full color', 'full color')], max_length=20),
        ),
        migrations.AlterField(
            model_name='portraitshot',
            name='shot',
            field=models.CharField(choices=[('halfbody', 'halfbody'), ('bust', 'bust'), ('wholebody', 'wholebody'), ('headshot', 'headshot')], max_length=20),
        ),
        migrations.AlterField(
            model_name='portraitshot',
            name='sizes',
            field=models.CharField(choices=[('3300 x 2550 px', '3300 x 2550 px'), ('2000 x 2000 px', '2000 x 2000 px'), ('3508 x 2480 px', '3508 x 2480 px')], max_length=20),
        ),
    ]
