# Generated by Django 4.0.6 on 2022-07-22 08:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('idx_js', models.IntegerField()),
                ('idx_html', models.IntegerField()),
                ('idx_image', models.ImageField(upload_to='')),
                ('idx_bool', models.BooleanField()),
                ('webpage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webpages.webpage')),
            ],
        ),
    ]
