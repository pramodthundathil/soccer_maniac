# Generated by Django 3.2.14 on 2023-09-12 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_fees_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Amount', models.FloatField()),
                ('Reason', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField()),
                ('Amount', models.FloatField()),
                ('Reason', models.CharField(max_length=1000)),
                ('Mode_Of_Payment', models.CharField(choices=[('Credit', 'Credit'), ('Cash', 'Cash'), ('Bank', 'Bank'), ('UPI', 'UPI')], max_length=255)),
                ('Cash_received', models.BooleanField(default=True)),
            ],
        ),
    ]
