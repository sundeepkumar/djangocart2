# Generated by Django 3.0.5 on 2020-07-13 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20200712_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.IntegerField(choices=[(0, 'Brand New'), (3, 'Used - Poor Condidtion'), (4, 'Used - Not Usable'), (1, 'Used - Like New'), (2, 'Used - Good')], default=4),
        ),
    ]
