# Generated by Django 3.0.5 on 2020-06-06 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctors', '0004_auto_20200606_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='current_visit',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='next_visit',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
