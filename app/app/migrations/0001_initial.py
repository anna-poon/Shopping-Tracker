# Generated by Django 4.2 on 2023-06-01 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Item",
            fields=[
                ("url", models.CharField(max_length=200)),
                ("item_name", models.AutoField(primary_key=True, serialize=False)),
                ("store", models.CharField(max_length=50)),
                ("price", models.CharField(max_length=50)),
                ("rating", models.IntegerField()),
            ],
        ),
    ]
