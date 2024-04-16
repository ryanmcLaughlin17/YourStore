# Generated by Django 4.1.7 on 2024-04-16 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0017_rename_chilled_item_sandwiches_and_prepared_food'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pastry_Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sku', models.IntegerField(default=0)),
                ('ingredients', models.TextField(max_length=1500)),
                ('vegan', models.BooleanField(default=False)),
                ('vegetarian', models.BooleanField(default=False)),
                ('time_in_box', models.CharField(default=False, max_length=20)),
                ('time_in_pastry_case', models.CharField(default=False, max_length=20)),
            ],
        ),
    ]
