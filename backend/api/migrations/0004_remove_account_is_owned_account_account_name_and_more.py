# Generated by Django 5.0.3 on 2024-04-30 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_owned',
        ),
        migrations.AddField(
            model_name='account',
            name='account_name',
            field=models.CharField(default='test', max_length=255, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='account',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='account',
            name='balance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12),
        ),
    ]
