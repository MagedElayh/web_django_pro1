# Generated by Django 3.1.3 on 2020-11-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0002_remove_month_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='month',
            name='period',
            field=models.ManyToManyField(to='mainpage.Period'),
        ),
    ]