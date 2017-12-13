# Generated by Django 2.0 on 2017-12-12 14:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deptname', models.CharField(max_length=50, verbose_name='Department Name')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('empid', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Employee ID')),
                ('facultyname', models.CharField(max_length=100, verbose_name='Faculty Name')),
                ('deptname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testmodelresapp.Department', verbose_name='Department Name')),
            ],
        ),
        migrations.CreateModel(
            name='JournalArticle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refformat', models.TextField(max_length=250, verbose_name='Citation Format')),
                ('jtitle', models.CharField(default='', max_length=200, verbose_name='Paper Title')),
                ('jname', models.CharField(default='', max_length=200, verbose_name='Journal Name')),
                ('jstatus', models.CharField(choices=[('Accepted', 'Accepted'), ('Submitted', 'Submitted'), ('Published', 'Published'), ('Under Review', 'Under Review')], default='Published', max_length=15, verbose_name='Publication Status')),
                ('jpublishedon', models.DateField(blank=True, verbose_name='Publication Date')),
                ('jvolno', models.IntegerField(blank=True, verbose_name='Volume')),
                ('jissueno', models.IntegerField(blank=True, verbose_name='ISSN NO')),
                ('jpageno', models.IntegerField(blank=True, verbose_name='Page No')),
                ('jtr', models.FloatField(blank=True, verbose_name='SCI-IF')),
                ('jsjr', models.FloatField(blank=True, verbose_name='SJR')),
                ('jsnip', models.FloatField(blank=True, verbose_name='SNIP')),
                ('jissn', models.IntegerField(blank=True, verbose_name='ISSN NO')),
                ('pubfromconf', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=5, verbose_name='Through conf.')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateField(null=True, verbose_name='Updated At')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='journals', to=settings.AUTH_USER_MODEL)),
                ('facultyauthor', models.ManyToManyField(max_length=100, to='testmodelresapp.Faculty', verbose_name='Faculty Author')),
            ],
        ),
        migrations.CreateModel(
            name='ResearchScholar',
            fields=[
                ('rsname', models.CharField(max_length=100, verbose_name='Student Name')),
                ('rsregno', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Registration Number')),
                ('deptname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testmodelresapp.Department', verbose_name='Department Name')),
                ('rssupervisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testmodelresapp.Faculty', verbose_name="Supervisor's Name")),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sregno', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='Registration Number')),
                ('sname', models.CharField(max_length=100, verbose_name='Student Name')),
                ('sbranch', models.CharField(max_length=50, verbose_name='Branch')),
                ('sbatch', models.CharField(max_length=20, verbose_name='Batch')),
                ('studentcategory', models.CharField(choices=[('UG Student', 'UG Student'), ('PG Student', 'PG Student')], default='UG Student', max_length=5, verbose_name='Student Category')),
                ('deptname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='testmodelresapp.Department', verbose_name='Department Name')),
            ],
        ),
        migrations.AddField(
            model_name='journalarticle',
            name='rsauthor',
            field=models.ManyToManyField(blank=True, max_length=100, to='testmodelresapp.ResearchScholar', verbose_name='Research Scholar Author'),
        ),
        migrations.AddField(
            model_name='journalarticle',
            name='studentauthor',
            field=models.ManyToManyField(blank=True, max_length=100, to='testmodelresapp.Student', verbose_name='Student Author'),
        ),
        migrations.AddField(
            model_name='journalarticle',
            name='updated_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
    ]
