# Generated by Django 3.0.5 on 2020-07-03 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200703_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='condition',
            field=models.IntegerField(choices=[(1, 'Used - Like New'), (2, 'Used - Good'), (4, 'Used - Not Usable'), (3, 'Used - Poor Condidtion'), (0, 'Brand New')], default=4),
        ),
    ]
