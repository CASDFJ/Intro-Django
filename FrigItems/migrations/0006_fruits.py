# Generated by Django 2.1.2 on 2018-10-23 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FrigItems', '0005_groceries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruits',
            fields=[
                ('fruit', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
