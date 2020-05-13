# Generated by Django 3.0.6 on 2020-05-08 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, unique=True)),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sem.Branch')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, unique=True)),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sem.Semester')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True, unique=True)),
                ('Quest', models.FileField(upload_to='quest')),
                ('Pdf', models.FileField(upload_to='pdfs')),
                ('Video', models.FileField(upload_to='videos')),
                ('branch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sem.Branch')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sem.Semester')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sem.Subject')),
            ],
        ),
    ]