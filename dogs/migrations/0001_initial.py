# Generated by Django 3.0.4 on 2020-03-09 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('Last_name', models.CharField(max_length=50)),
                ('photo', models.ImageField(upload_to='photo/%Y/%m/%d/')),
                ('comment', models.CharField(max_length=500)),
                ('city', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=30)),
            ],
        ),
    ]
