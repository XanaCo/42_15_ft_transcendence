# Generated by Django 5.0.3 on 2024-03-29 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WaitingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userID', models.IntegerField()),
                ('userName', models.CharField(max_length=200)),
                ('waitingTime', models.TimeField(auto_now_add=True)),
                ('position', models.IntegerField()),
                ('game', models.CharField(choices=[('pkm_multiplayer', 'Pokemon - Multiplayer'), ('pong_multiplayer', 'Pong - Multiplayer'), ('pong_tournament', 'Pong - Tournament')], max_length=200)),
            ],
        ),
    ]
