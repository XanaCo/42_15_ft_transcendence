# Generated by Django 5.0.3 on 2024-03-29 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('arena', '0003_species'),
    ]

    operations = [
        migrations.RenameField(
            model_name='elem',
            old_name='attElemFlote',
            new_name='attElemFlotte',
        ),
    ]
