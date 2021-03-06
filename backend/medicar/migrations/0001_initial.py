# Generated by Django 3.1.1 on 2020-09-29 03:04

from django.conf import settings
import django.contrib.postgres.fields
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField(verbose_name='Dia')),
                ('schedule', django.contrib.postgres.fields.ArrayField(base_field=models.TimeField(verbose_name='Horários'), size=None)),
            ],
            options={
                'verbose_name': 'Agenda',
                'verbose_name_plural': 'Agendas',
                'ordering': ['day'],
            },
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Nome')),
            ],
            options={
                'verbose_name': 'Especialidade',
                'verbose_name_plural': 'Especialidades',
                'ordering': ['id', 'name'],
            },
        ),
        migrations.CreateModel(
            name='MedicalAppointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hourly', models.TimeField(verbose_name='Horários')),
                ('scheduling_date', models.DateTimeField(auto_now_add=True, verbose_name='Data de agendamento')),
                ('agenda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agenda_medical_appointment', to='medicar.agenda', verbose_name='Agenda')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_medical_appointment', to=settings.AUTH_USER_MODEL, verbose_name='Paciente')),
            ],
            options={
                'verbose_name': 'Consulta',
                'verbose_name_plural': 'Consultas',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55, verbose_name='Nome')),
                ('crm', models.IntegerField(verbose_name='CRM')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+9999999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')], verbose_name='Telefone')),
                ('specialty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor', to='medicar.specialty', verbose_name='Especialidade')),
            ],
            options={
                'verbose_name': 'Médico',
                'verbose_name_plural': 'Médicos',
                'ordering': ['id', 'name'],
            },
        ),
        migrations.AddField(
            model_name='agenda',
            name='doctor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='agenda', to='medicar.doctor', verbose_name='Médico'),
        ),
    ]
