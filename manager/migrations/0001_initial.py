# Generated by Django 4.1.7 on 2023-03-13 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('password', models.CharField(max_length=64)),
                ('gender', models.SmallIntegerField(choices=[(1, '男'), (2, '女')])),
                ('salary', models.DateTimeField(default=0, max_length=10)),
                ('depart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.department')),
            ],
        ),
    ]
