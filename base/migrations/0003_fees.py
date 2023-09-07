# Generated by Django 3.2.14 on 2023-09-07 04:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20230906_0733'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fee_amount', models.FloatField()),
                ('date', models.DateField()),
                ('mode', models.CharField(choices=[('Cash', 'Cash'), ('Bank', 'Bank'), ('UPI', 'UPI')], max_length=25)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.studentdetails')),
            ],
        ),
    ]