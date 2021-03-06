# Generated by Django 2.0.4 on 2018-05-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_order'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.RemoveField(
            model_name='order',
            name='amount',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phonenumber',
        ),
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default='DEFAULT VALUE', max_length=1500),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='DEFAULT VALUE', max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='address',
            field=models.CharField(default='DEFAULT VALUE', max_length=1500),
        ),
    ]
