# Generated by Django 4.2.4 on 2024-03-25 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrganApp', '0019_registration_last_donate_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registration',
            old_name='name',
            new_name='fname',
        ),
        migrations.AddField(
            model_name='registration',
            name='lname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
