# Generated by Django 4.1.5 on 2023-01-14 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_homeadmiddlebanner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homeadmiddlebanner',
            name='title',
        ),
        migrations.AddField(
            model_name='homeadmiddlebanner',
            name='title_first_part',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='homeadmiddlebanner',
            name='title_second_part',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]