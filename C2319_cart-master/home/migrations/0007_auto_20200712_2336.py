# Generated by Django 3.0.5 on 2020-07-13 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20200712_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.IntegerField(choices=[(1, 'Used - Like New'), (3, 'Used - Poor Condidtion'), (4, 'Used - Not Usable'), (0, 'Brand New'), (2, 'Used - Good')], default=4),
        ),
    ]