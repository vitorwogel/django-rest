# Generated by Django 4.2.3 on 2023-07-28 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_person_remove_item_created_item_count_item_price_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='items',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
