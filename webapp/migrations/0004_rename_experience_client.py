# Generated by Django 4.2.7 on 2023-12-09 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_experience_alter_employee_email'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Experience',
            new_name='Client',
        ),
    ]
