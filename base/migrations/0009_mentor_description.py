# Generated by Django 3.0.5 on 2020-04-13 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20200413_1717'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='description',
            field=models.CharField(max_length=500, null=True),
        ),
    ]