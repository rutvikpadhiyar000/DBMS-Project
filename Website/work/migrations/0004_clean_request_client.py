# Generated by Django 3.2 on 2021-04-27 05:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_auto_20210427_0502'),
        ('work', '0003_auto_20210426_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='clean_request',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='client.client'),
        ),
    ]
