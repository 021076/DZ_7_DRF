# Generated by Django 5.0.6 on 2024-07-02 15:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payments',
            name='date_payment',
            field=models.DateField(auto_now=True, verbose_name='Дата оплаты'),
        ),
    ]