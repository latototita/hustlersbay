# Generated by Django 3.2 on 2022-11-28 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_balance_top'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='date_deposited',
            field=models.DateTimeField(),
        ),
    ]
