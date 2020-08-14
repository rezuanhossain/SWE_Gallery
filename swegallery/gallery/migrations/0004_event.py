# Generated by Django 3.0.8 on 2020-08-14 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('name', models.CharField(max_length=250)),
                ('date', models.DateField(auto_now_add=True)),
                ('desc', models.TextField()),
            ],
        ),
    ]