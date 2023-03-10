# Generated by Django 4.0 on 2023-01-16 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='MiniCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(default='super_category.png', help_text='Please use our recommended dimensions: 120px X 120px', upload_to='images/category/mini/')),
                ('slug', models.SlugField(max_length=250, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('main_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_in_mini', to='home.maincategory')),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_in_mini', to='home.maincategory')),
                ('super_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='super_in_mini', to='home.supercategory')),
            ],
            options={
                'verbose_name_plural': 'Categories mini',
            },
        ),
    ]
