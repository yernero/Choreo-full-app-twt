# Generated by Django 5.0.3 on 2024-04-30 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_remove_customer_customer_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='currency',
            field=models.CharField(default='USD', max_length=10),
            preserve_default=False,
        ),
    ]
