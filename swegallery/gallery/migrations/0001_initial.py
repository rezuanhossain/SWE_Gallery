# Generated by Django 3.0.8 on 2020-07-18 20:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('registration', '0002_auto_20200719_0252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
                ('list_date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('photo_main', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('photo1', models.ImageField(blank=True, upload_to='photos/%y/%m/%d')),
                ('photos2', models.ImageField(blank=True, upload_to='photos/%y/%m/%d')),
                ('photos3', models.ImageField(blank=True, upload_to='photos/%y/%m/%d')),
                ('photos4', models.ImageField(blank=True, upload_to='photos/%y/%m/%d')),
                ('photos5', models.ImageField(blank=True, upload_to='photos/%y/%m/%d')),
                ('photos6', models.ImageField(blank=True, upload_to='photos/%y/%m/%d')),
                ('admin_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registration.User')),
            ],
            options={
                'ordering': ('-list_date',),
            },
        ),
    ]
