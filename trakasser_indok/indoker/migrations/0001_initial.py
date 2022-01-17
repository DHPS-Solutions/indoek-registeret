# Generated by Django 4.0 on 2022-01-17 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Indoker',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fname', models.CharField(max_length=32)),
                ('sname', models.CharField(max_length=32)),
                ('slug', models.SlugField()),
                ('profile_pic', models.ImageField(default='path/to/my/default/image.jpg', upload_to='')),
            ],
        ),
    ]