# Generated by Django 3.0.8 on 2020-07-28 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='photo1',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='photos2',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='photos3',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='photos4',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='photos5',
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='photos6',
        ),
        migrations.CreateModel(
            name='all_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('gallery', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='gallery.Gallery')),
            ],
        ),
    ]
