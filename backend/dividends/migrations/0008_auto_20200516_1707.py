# Generated by Django 3.0.6 on 2020-05-16 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dividends', '0007_stock_ex_div_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='ex_div_date',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]