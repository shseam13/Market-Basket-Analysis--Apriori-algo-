# Generated by Django 4.1.4 on 2022-12-29 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_rename_contact_date_contact_purchase_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='product_id',
            field=models.IntegerField(),
        ),
    ]
