# Generated by Django 2.2.7 on 2019-12-05 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evals', '0012_auto_20191205_1726'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessionscore',
            name='judgeName',
        ),
        migrations.RemoveField(
            model_name='teamscore',
            name='judgeName',
        ),
    ]
