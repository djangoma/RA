# Generated by Django 2.0 on 2017-12-14 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmodelresapp', '0009_auto_20171214_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalarticle',
            name='jsjr',
            field=models.FloatField(blank=True, null=True, verbose_name='SJR'),
        ),
        migrations.AlterField(
            model_name='journalarticle',
            name='jsnip',
            field=models.FloatField(blank=True, null=True, verbose_name='SNIP'),
        ),
        migrations.AlterField(
            model_name='journalarticle',
            name='jtr',
            field=models.FloatField(blank=True, null=True, verbose_name='SCI-IF'),
        ),
    ]
