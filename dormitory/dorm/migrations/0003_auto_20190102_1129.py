# Generated by Django 2.1.4 on 2019-01-02 03:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dorm', '0002_visitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='floor_num',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='building',
            name='start_time',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='contact',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='room',
            name='cost',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='buildingid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dorm.Building'),
        ),
        migrations.AddField(
            model_name='student',
            name='collegeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dorm.College'),
        ),
        migrations.AddField(
            model_name='student',
            name='nation',
            field=models.CharField(max_length=20, null=True),
        ),
    ]