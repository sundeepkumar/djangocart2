# Generated by Django 3.0.5 on 2020-07-13 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200703_0123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.IntegerField(choices=[(2, 'Used - Good'), (0, 'Brand New'), (4, 'Used - Not Usable'), (1, 'Used - Like New'), (3, 'Used - Poor Condidtion')], default=4),
        ),
    ]
