# Generated by Django 4.2.3 on 2023-07-28 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_person_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='items',
            field=models.TextField(null=True),
        ),
    ]