# Generated by Django 2.0.5 on 2018-08-01 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CPModel_2', '0002_auto_20180801_2338'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newsarticle',
            old_name='urlid',
            new_name='_id',
        ),
    ]