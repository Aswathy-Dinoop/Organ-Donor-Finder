# Generated by Django 4.2.4 on 2024-03-25 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrganApp', '0020_rename_name_registration_fname_registration_lname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blood_donation',
            name='donateblood',
        ),
        migrations.AddField(
            model_name='organ_donation',
            name='hospitalaname',
            field=models.CharField(max_length=75, null=True),
        ),
        migrations.AddField(
            model_name='organ_donation',
            name='status',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
