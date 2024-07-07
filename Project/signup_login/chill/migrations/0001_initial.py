# Generated by Django 5.0.1 on 2024-02-07 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('stream', models.CharField(max_length=50)),
                ('marks', models.IntegerField()),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
