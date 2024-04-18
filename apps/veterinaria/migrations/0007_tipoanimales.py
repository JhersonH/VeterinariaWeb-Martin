# Generated by Django 4.1.7 on 2024-04-18 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('veterinaria', '0006_remove_visita_anexo_mascota_visita_mascota_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoAnimales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, max_length=50, null=True, verbose_name='Tipo de Animal')),
                ('fecha_hora_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de Creación')),
                ('fecha_hora_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha y Hora de Modificación')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UsercreacionTipoAnimal', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UserModTipoAnimal', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tipo de Animal',
                'verbose_name_plural': 'Tipo de Animal',
            },
        ),
    ]