# Generated by Django 2.1.4 on 2019-01-01 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('amount', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': '班级',
            },
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': '专业',
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False, verbose_name='工号')),
                ('user_real_name', models.CharField(max_length=20, verbose_name='姓名')),
                ('user_password', models.CharField(max_length=18, verbose_name='密码')),
                ('user_type', models.CharField(max_length=20, verbose_name='权限')),
            ],
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('item', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('book_dt', models.DateTimeField()),
                ('reason', models.TextField(null=True)),
                ('fix_dt', models.DateTimeField(null=True)),
                ('remark', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('name', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('room_type', models.CharField(max_length=20, null=True)),
                ('capacity', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('roomid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dorm.Room')),
                ('remain', models.FloatField()),
            ],
            options={
                'verbose_name_plural': '电费余额',
            },
        ),
        migrations.CreateModel(
            name='FeeRecord',
            fields=[
                ('roomid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dorm.Room')),
                ('dt', models.DateTimeField()),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Housemaster',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dorm.Owner')),
                ('name', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=200, null=True)),
                ('buildingid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dorm.Building')),
            ],
            options={
                'verbose_name_plural': '舍管',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dorm.Owner')),
                ('name', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': '导员',
            },
        ),
        migrations.CreateModel(
            name='Maintenance',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dorm.Owner')),
                ('name', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('roomid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dorm.Room')),
                ('dt', models.DateTimeField()),
                ('score', models.FloatField()),
                ('remark', models.TextField(null=True)),
                ('housemasterid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorm.Housemaster')),
            ],
        ),
        migrations.CreateModel(
            name='Secretary',
            fields=[
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dorm.Owner')),
                ('name', models.CharField(max_length=20)),
                ('contact', models.CharField(max_length=200, null=True)),
                ('collegeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorm.College')),
            ],
            options={
                'verbose_name_plural': '书记',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dorm.Owner')),
                ('name', models.CharField(max_length=20)),
                ('sex', models.NullBooleanField()),
                ('contact', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': '学生',
            },
        ),
        migrations.AddField(
            model_name='room',
            name='buildingid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorm.Building'),
        ),
        migrations.AddField(
            model_name='repair',
            name='roomid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorm.Room'),
        ),
        migrations.AddField(
            model_name='class',
            name='collegeid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dorm.College'),
        ),
        migrations.CreateModel(
            name='EnterApply',
            fields=[
                ('sno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dorm.Student')),
                ('dt', models.DateTimeField()),
                ('housemaster_check', models.NullBooleanField()),
                ('instructor_check', models.NullBooleanField()),
                ('secretary_check', models.NullBooleanField()),
                ('roomid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorm.Room')),
            ],
        ),
        migrations.CreateModel(
            name='LiveRecord',
            fields=[
                ('sno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dorm.Student')),
                ('enter_time', models.DateTimeField()),
                ('quit_time', models.DateTimeField(null=True)),
                ('roomid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorm.Room')),
            ],
        ),
        migrations.CreateModel(
            name='QuitApply',
            fields=[
                ('sno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='dorm.Student')),
                ('dt', models.DateTimeField()),
                ('reason', models.TextField()),
                ('housemaster_check', models.NullBooleanField()),
                ('instructor_check', models.NullBooleanField()),
                ('secretary_check', models.NullBooleanField()),
                ('roomid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dorm.Room')),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='classid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dorm.Class'),
        ),
        migrations.AddField(
            model_name='student',
            name='roomid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dorm.Room'),
        ),
        migrations.AddField(
            model_name='repair',
            name='maintenanceid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dorm.Maintenance'),
        ),
        migrations.AlterUniqueTogether(
            name='feerecord',
            unique_together={('roomid', 'dt')},
        ),
        migrations.AddField(
            model_name='class',
            name='instructorid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dorm.Instructor'),
        ),
        migrations.AlterUniqueTogether(
            name='repair',
            unique_together={('item', 'roomid', 'book_dt')},
        ),
        migrations.AlterUniqueTogether(
            name='mark',
            unique_together={('roomid', 'dt')},
        ),
        migrations.AlterUniqueTogether(
            name='quitapply',
            unique_together={('sno', 'roomid', 'dt')},
        ),
        migrations.AlterUniqueTogether(
            name='liverecord',
            unique_together={('sno', 'roomid', 'enter_time')},
        ),
        migrations.AlterUniqueTogether(
            name='enterapply',
            unique_together={('sno', 'roomid', 'dt')},
        ),
    ]
