# Generated by Django 4.2.6 on 2023-11-02 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('component1', '0002_userdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='confimr',
            field=models.CharField(default=True, max_length=130),
        ),
    ]
