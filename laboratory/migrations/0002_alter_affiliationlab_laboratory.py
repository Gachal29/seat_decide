# Generated by Django 4.2 on 2023-04-25 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='affiliationlab',
            name='laboratory',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='laboratory.laboratory'),
        ),
    ]
