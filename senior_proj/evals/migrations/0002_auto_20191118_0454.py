# Generated by Django 2.2.7 on 2019-11-18 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('evals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='judgeName',
            field=models.CharField(default='me', max_length=50),
        ),
        migrations.AlterField(
            model_name='post',
            name='groupName',
            field=models.CharField(max_length=50),
        ),
    ]
