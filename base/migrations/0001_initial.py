# Generated by Django 3.2.14 on 2023-09-05 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(max_length=255)),
                ('Date_of_Birth', models.DateField()),
                ('Address', models.TextField()),
                ('Phone_Number', models.CharField(max_length=15)),
                ('Email', models.EmailField(max_length=254)),
                ('Parents_Mobile_Number', models.CharField(max_length=15)),
                ('Blood_Group', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], max_length=20)),
                ('ID_Proof_Submitted', models.BooleanField(default=True)),
                ('Type_Of_Id_Proof', models.CharField(choices=[('Aadhaar', 'Aadhaar'), ('Driving License', 'Driving License'), ('Voter Id', 'Voter Id'), ('PanCard', 'Pancard'), ('School Id', 'Scool Id'), ('Other', 'Other'), ('Not Submitted', 'Not Submitted')], max_length=20)),
                ('Class_Studing', models.CharField(max_length=255)),
                ('School', models.CharField(max_length=255)),
                ('School_Timeing', models.CharField(max_length=255)),
                ('Date_of_Joining', models.DateField()),
                ('Date_of_Leaving', models.DateField(blank=True, null=True)),
                ('Course_Duration_In_Months', models.IntegerField()),
                ('Total_Fee', models.FloatField()),
                ('Discount', models.IntegerField(blank=True, null=True)),
                ('Fee_Installments', models.FloatField()),
                ('Live_Status', models.BooleanField(default=True)),
            ],
        ),
    ]
