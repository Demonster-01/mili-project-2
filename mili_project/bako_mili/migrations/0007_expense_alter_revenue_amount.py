# Generated by Django 4.2.9 on 2024-01-13 07:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("bako_mili", "0006_rename_payer_revenue_payer"),
    ]

    operations = [
        migrations.CreateModel(
            name="expense",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=30)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "transaction_date",
                    models.DateField(default=django.utils.timezone.now),
                ),
                ("remark", models.CharField(max_length=50, null=True)),
                ("image", models.ImageField(null=True, upload_to="expense_bill_pics")),
            ],
        ),
        migrations.AlterField(
            model_name="revenue",
            name="amount",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
