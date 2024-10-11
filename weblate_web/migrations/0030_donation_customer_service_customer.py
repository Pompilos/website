# Generated by Django 5.0.6 on 2024-10-11 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0028_alter_customer_email"),
        ("weblate_web", "0029_package_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="donation",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="payments.customer",
            ),
        ),
        migrations.AddField(
            model_name="service",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="payments.customer",
            ),
        ),
    ]
