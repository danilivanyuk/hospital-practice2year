# Generated by Django 3.0.5 on 2020-06-06 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0005_auto_20200606_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='additionalInfo',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
