# Generated by Django 4.0 on 2022-01-17 21:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('indoker', '0002_alter_indoker_profile_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='indoker',
            old_name='sname',
            new_name='etternavn',
        ),
        migrations.RenameField(
            model_name='indoker',
            old_name='fname',
            new_name='fornavn',
        ),
        migrations.AddField(
            model_name='indoker',
            name='facebooklink',
            field=models.CharField(default=django.utils.timezone.now, max_length=130),
            preserve_default=False,
        ),
    ]
