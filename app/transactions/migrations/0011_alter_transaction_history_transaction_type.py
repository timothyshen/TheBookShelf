# Generated by Django 3.2.7 on 2021-09-12 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0010_income_history_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction_history',
            name='Transaction_type',
            field=models.CharField(choices=[('Transfer', 'Transfer'), ('Purchased Chapter', 'Purchased Chapter'), ('Purchased item', 'Purchased item'), ('Donation', 'Donation')], default=None, max_length=20),
        ),
    ]