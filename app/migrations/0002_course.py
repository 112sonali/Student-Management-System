# Generated by Django 5.0.4 on 2024-05-02 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=100)),
                ('fees', models.IntegerField()),
                ('duration', models.CharField(max_length=100)),
            ],
        ),
    ]
