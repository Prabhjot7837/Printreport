# Generated by Django 4.0.2 on 2022-11-10 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Potholedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.TextField()),
                ('Road_condition', models.CharField(choices=[('bad', 'Bad'), ('good', 'Good'), ('danger', 'Dangerous'), ('very_bad', 'Deadly_bad')], max_length=10)),
                ('kms_covered', models.IntegerField()),
                ('anomalies_detected', models.IntegerField()),
                ('pothole', models.IntegerField()),
                ('cracks', models.IntegerField()),
                ('patches', models.IntegerField()),
            ],
        ),
    ]