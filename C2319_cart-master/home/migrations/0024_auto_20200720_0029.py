# Generated by Django 3.0.5 on 2020-07-20 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20200720_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='condition',
            field=models.IntegerField(choices=[(4, 'Used - Not Usable'), (1, 'Used - Like New'), (2, 'Used - Good'), (3, 'Used - Poor Condidtion'), (0, 'Brand New')], default=4),
        ),
    ]
