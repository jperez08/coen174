# Generated by Django 2.2.7 on 2019-12-05 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evals', '0014_auto_20191205_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionscore',
            name='judgeName',
            field=models.CharField(default='NA', max_length=20),
        ),
        migrations.AlterField(
            model_name='teamscore',
            name='teamName',
            field=models.CharField(default='NA', max_length=20),
        ),
    ]
