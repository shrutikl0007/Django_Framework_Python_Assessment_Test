# Generated by Django 5.0.1 on 2024-02-06 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0011_auto_20200508_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='notice',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
