# Generated by Django 4.2.7 on 2023-12-05 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_remove_userprofile_buildingid_userprofile_building_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='flatNumber',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='telephone',
            field=models.CharField(max_length=30, null=True),
        ),
    ]