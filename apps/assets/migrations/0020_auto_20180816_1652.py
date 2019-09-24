# Generated by Django 2.0.7 on 2018-08-16 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0019_auto_20180816_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adminuser',
            name='org_id',
            field=models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='org_id',
            field=models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization'),
        ),
        migrations.AlterField(
            model_name='domain',
            name='org_id',
            field=models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization'),
        ),
        migrations.AlterField(
            model_name='gateway',
            name='org_id',
            field=models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization'),
        ),
        migrations.AlterField(
            model_name='label',
            name='org_id',
            field=models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization'),
        ),
        migrations.AlterField(
            model_name='node',
            name='org_id',
            field=models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization'),
        ),
        migrations.AlterField(
            model_name='systemuser',
            name='org_id',
            field=models.CharField(blank=True, db_index=True, default='', max_length=36, verbose_name='Organization'),
        ),
    ]
