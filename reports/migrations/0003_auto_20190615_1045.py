# Generated by Django 2.2.2 on 2019-06-15 10:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0002_auto_20190613_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='campaign',
            name='invoice',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reports.Invoice'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='campaign',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='total',
            field=models.FloatField(default=0),
        ),
        migrations.DeleteModel(
            name='InvoiceRow',
        ),
    ]