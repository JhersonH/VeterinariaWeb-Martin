# Generated by Django 4.1.7 on 2024-04-27 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('veterinaria', '0011_remove_visita_usuario_creacion_mascota_archivo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiaclinica',
            name='anexo_doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='AnexoDoctor', to='veterinaria.doctor'),
        ),
    ]
