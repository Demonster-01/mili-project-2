# Generated by Django 4.2.9 on 2024-01-12 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("bako_mili", "0005_rename_customer_revenue_payer"),
    ]

    operations = [
        migrations.RenameField(
            model_name="revenue",
            old_name="Payer",
            new_name="payer",
        ),
    ]
