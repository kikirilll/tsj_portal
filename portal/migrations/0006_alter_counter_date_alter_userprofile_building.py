# Generated by Django 4.2.7 on 2023-12-08 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0005_alter_userprofile_flatnumber_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counter',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='building',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portal.building'),
        ),
    ]
