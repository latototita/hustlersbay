# Generated by Django 3.2 on 2022-11-18 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_auto_20221118_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='balance',
            name='amount',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='currencie',
            name='name',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='amount',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='person',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='transID',
            field=models.CharField(default=1, max_length=1000),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='txt_random',
            field=models.CharField(default=1, max_length=1000),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='wallet',
            field=models.CharField(default=1, max_length=1000),
        ),
        migrations.AlterField(
            model_name='earning',
            name='person',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='referralbonu',
            name='person',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='referred',
            name='personrefferred',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='amount',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='person',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='phone',
            field=models.CharField(default=1, max_length=1000),
        ),
        migrations.AlterField(
            model_name='withdrawal',
            name='txt_random',
            field=models.CharField(default=1, max_length=1000),
        ),
    ]
