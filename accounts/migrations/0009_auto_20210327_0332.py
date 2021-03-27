# Generated by Django 3.1.7 on 2021-03-27 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customer_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amount',
            name='balance',
        ),
        migrations.RemoveField(
            model_name='amount',
            name='withdrawn',
        ),
        migrations.AddField(
            model_name='customer',
            name='withdrawn',
            field=models.IntegerField(null=True),
        ),
    ]