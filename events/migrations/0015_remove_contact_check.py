# Generated by Django 2.2.5 on 2019-09-12 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0014_contact_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='check',
        ),
    ]
