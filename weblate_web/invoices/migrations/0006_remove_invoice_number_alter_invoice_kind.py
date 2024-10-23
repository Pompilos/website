# Generated by Django 5.1.2 on 2024-10-23 11:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("invoices", "0005_alter_invoice_currency_alter_invoice_number"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="invoice",
            name="number",
        ),
        migrations.AlterField(
            model_name="invoice",
            name="kind",
            field=models.IntegerField(
                choices=[(0, "Draft"), (10, "Invoice"), (50, "Proforma"), (90, "Quote")]
            ),
        ),
    ]
