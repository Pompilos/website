# Generated by Django 5.1.2 on 2024-10-18 09:41

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("payments", "0031_alter_payment_customer_alter_payment_paid_invoice_and_more"),
        ("weblate_web", "0031_fill_in_customer"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="donation",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="payments.customer",
            ),
        ),
        migrations.AlterField(
            model_name="donation",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="pastpayments",
            name="donation",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="weblate_web.donation",
            ),
        ),
        migrations.AlterField(
            model_name="pastpayments",
            name="subscription",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="weblate_web.subscription",
            ),
        ),
        migrations.AlterField(
            model_name="service",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="payments.customer",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="package",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="weblate_web.package"
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="weblate_web.service"
            ),
        ),
    ]
