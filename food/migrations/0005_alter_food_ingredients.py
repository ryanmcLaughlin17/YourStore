# Generated by Django 4.1.7 on 2024-04-14 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_alter_food_ingredients'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='ingredients',
            field=models.TextField(max_length=750),
        ),
    ]
