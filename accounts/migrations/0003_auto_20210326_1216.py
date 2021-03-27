# Generated by Django 3.1.7 on 2021-03-26 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_amount_earning'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='amount',
            name='earned',
        ),
        migrations.AddField(
            model_name='amount',
            name='person',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer'),
        ),
        migrations.AddField(
            model_name='earning',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer'),
        ),
        migrations.AddField(
            model_name='earning',
            name='money',
            field=models.IntegerField(null=True),
        ),
    ]
