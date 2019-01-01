# Generated by Django 2.1.4 on 2019-01-01 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dorm', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visitor',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('sex', models.BooleanField()),
                ('document_type', models.CharField(max_length=20, null=True)),
                ('documentno', models.CharField(max_length=20, null=True)),
                ('contact', models.CharField(max_length=200, null=True)),
                ('dt', models.DateTimeField()),
                ('housemasterid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorm.Housemaster')),
            ],
        ),
    ]
