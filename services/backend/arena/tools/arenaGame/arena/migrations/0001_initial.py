# Generated by Django 5.0.3 on 2024-03-29 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='elem',
            fields=[
                ('name', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('attElemFlote', models.IntegerField()),
                ('attElemFeuille', models.IntegerField()),
                ('attElemChaud', models.IntegerField()),
                ('attElemBrise', models.IntegerField()),
                ('attElemSable', models.IntegerField()),
                ('attElemBagarre', models.IntegerField()),
                ('attElemCaillou', models.IntegerField()),
            ],
        ),
    ]
