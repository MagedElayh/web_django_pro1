# Generated by Django 3.1.3 on 2020-11-13 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frist_name', models.CharField(max_length=20, verbose_name="Doctor's first name")),
                ('last_name', models.CharField(max_length=20, verbose_name="Doctor's last name")),
                ('phone', models.PositiveIntegerField()),
                ('city', models.CharField(blank=True, max_length=15, null=True)),
                ('country', models.CharField(blank=True, max_length=15, null=True)),
                ('mail', models.EmailField(max_length=254, verbose_name='email')),
                ('date_entry', models.DateField(blank=True, null=True, verbose_name='date entry')),
                ('date_out', models.DateField(blank=True, null=True, verbose_name='date entry')),
            ],
        ),
        migrations.CreateModel(
            name='Period',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_from', models.TimeField(verbose_name='time period start')),
                ('time_to', models.TimeField(verbose_name='time period end')),
                ('doctor', models.ManyToManyField(to='mainpage.Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Month',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_number', models.PositiveIntegerField(unique=True, verbose_name='number of month')),
                ('days', models.DateField(unique=True)),
                ('period', models.ManyToManyField(to='mainpage.Period')),
            ],
        ),
    ]