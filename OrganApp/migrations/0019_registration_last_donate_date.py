# Generated by Django 4.2.4 on 2024-03-12 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OrganApp', '0018_alter_organ_donation_lastorgandonationdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='registration',
            name='last_donate_date',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
