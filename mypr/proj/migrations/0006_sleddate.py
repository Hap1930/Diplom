# Generated by Django 5.0.3 on 2024-04-23 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proj', '0005_alter_computers_employeeid_alter_monitors_employeeid_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SledDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
    ]
