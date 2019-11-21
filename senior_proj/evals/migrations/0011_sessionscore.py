# Generated by Django 2.2.7 on 2019-11-21 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evals', '0010_teamscore_total'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline', models.CharField(default='NA', max_length=50)),
                ('score1', models.IntegerField()),
                ('score2', models.IntegerField()),
                ('score3', models.IntegerField()),
                ('score4', models.IntegerField()),
                ('score5', models.IntegerField()),
                ('score6', models.IntegerField()),
                ('score7', models.IntegerField()),
                ('score8', models.IntegerField()),
                ('score9', models.IntegerField()),
                ('score10', models.IntegerField()),
                ('score11', models.IntegerField()),
                ('score12', models.IntegerField()),
                ('total', models.IntegerField()),
                ('comments', models.TextField()),
            ],
        ),
    ]
