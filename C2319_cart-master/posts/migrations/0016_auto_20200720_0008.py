# Generated by Django 3.0.5 on 2020-07-20 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0015_auto_20200720_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(0, 'Brand New'), (1, 'Used - Like New'), (2, 'Used - Good'), (3, 'Used - Poor Condidtion'), (4, 'Used - Not Usable')], default=4),
        ),
    ]
