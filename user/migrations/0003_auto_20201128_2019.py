# Generated by Django 3.1.3 on 2020-11-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20201128_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uname',
            field=models.CharField(max_length=100),
        ),
    ]
