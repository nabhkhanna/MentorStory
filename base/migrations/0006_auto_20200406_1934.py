# Generated by Django 3.0.5 on 2020-04-06 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_mentee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentee',
            name='firstName',
            field=models.CharField(default='mentee first name', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mentee',
            name='lastName',
            field=models.CharField(default='mentee last name', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='firstName',
            field=models.CharField(default='mentor first name', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='lastName',
            field=models.CharField(default='mentor last name', max_length=200, null=True),
        ),
    ]
