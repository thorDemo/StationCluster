# Generated by Django 2.0.5 on 2018-08-01 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CPModel_2', '0004_auto_20180801_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='listarticle',
            name='list_ch',
            field=models.CharField(default='美食', max_length=100),
        ),
    ]