# Generated by Django 3.0.6 on 2020-05-15 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sem', '0002_branch_branch_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='course', to='sem.Subject'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='semesters', to='sem.Branch'),
        ),
        migrations.AlterField(
            model_name='subject',
            name='semester',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='sem.Semester'),
        ),
    ]
