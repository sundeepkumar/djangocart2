# Generated by Django 3.0.5 on 2021-01-26 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0036_auto_20200731_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(4, 'Used - Not Usable'), (2, 'Used - Good'), (0, 'Brand New'), (3, 'Used - Poor Condidtion'), (1, 'Used - Like New')], default=4),
        ),
    ]