# Generated by Django 5.0.3 on 2024-03-29 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arena', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='attack',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('power', models.IntegerField()),
                ('elem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='arena.elem')),
            ],
        ),
    ]
