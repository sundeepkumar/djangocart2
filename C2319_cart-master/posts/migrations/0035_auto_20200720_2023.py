# Generated by Django 3.0.5 on 2020-07-21 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0034_auto_20200720_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(3, 'Used - Poor Condidtion'), (2, 'Used - Good'), (1, 'Used - Like New'), (0, 'Brand New'), (4, 'Used - Not Usable')], default=4),
        ),
    ]