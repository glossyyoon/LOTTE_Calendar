# Generated by Django 3.0.6 on 2020-10-19 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('email', models.EmailField(max_length=100, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
