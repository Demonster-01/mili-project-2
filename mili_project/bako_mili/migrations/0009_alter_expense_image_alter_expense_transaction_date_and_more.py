# Generated by Django 4.2.9 on 2024-01-13 16:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bako_mili", "0008_alter_expense_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="expense",
            name="image",
            field=models.ImageField(
                blank=True, null=True, upload_to="expense_bill_pics/"
            ),
        ),
        migrations.AlterField(
            model_name="expense",
            name="transaction_date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 1, 13, 16, 37, 20, 814728, tzinfo=datetime.timezone.utc
                )
            ),
        ),
        migrations.AlterField(
            model_name="revenue",
            name="transaction_date",
            field=models.DateField(
                default=datetime.datetime(
                    2024, 1, 13, 16, 37, 20, 814728, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]