# Generated by Django 3.1.1 on 2020-10-07 01:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('medicar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agenda', to='medicar.doctor', verbose_name='Médico'),
        ),
    ]
