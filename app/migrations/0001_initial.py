# Generated by Django 4.1.4 on 2023-01-21 05:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('Empno', models.IntegerField(primary_key=True, serialize=False)),
                ('Ename', models.CharField(max_length=20)),
                ('Deptno', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Loc', models.CharField(max_length=20)),
                ('Deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.emp')),
            ],
        ),
    ]
