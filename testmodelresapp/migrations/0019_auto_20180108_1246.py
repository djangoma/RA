# Generated by Django 2.0 on 2018-01-08 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testmodelresapp', '0018_document'),
    ]

    operations = [
        migrations.AlterField(
            model_name='journalarticle',
            name='jpublishedon',
            field=models.DateField(blank=True, null=True, verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='project',
            name='amountreceived',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Amount Received'),
        ),
        migrations.AlterField(
            model_name='project',
            name='fundreleasedon',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Fund Released On'),
        ),
        migrations.AlterField(
            model_name='project',
            name='sanctionedamount',
            field=models.FloatField(blank=True, null=True, verbose_name='Sanctioned Amount'),
        ),
    ]