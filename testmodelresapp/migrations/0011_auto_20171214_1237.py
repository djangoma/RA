# Generated by Django 2.0 on 2017-12-14 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmodelresapp', '0010_auto_20171214_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalarticle',
            name='jissn',
            field=models.IntegerField(blank=True, null=True, verbose_name='ISSN NO'),
        ),
    ]
