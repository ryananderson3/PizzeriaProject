# Generated by Django 3.0.5 on 2022-11-27 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('PizzasApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toppings',
            name='pizza',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PizzasApp.Pizza'),
        ),
    ]