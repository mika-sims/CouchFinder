# Generated by Django 3.2 on 2023-06-12 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20230612_0248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuserprofile',
            name='bio',
            field=models.TextField(blank=True, default=''),
        ),
    ]
