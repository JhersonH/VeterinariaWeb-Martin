# Generated by Django 4.1.7 on 2024-03-28 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('veterinaria', '0002_tratamientosslider'),
    ]

    operations = [
        migrations.CreateModel(
            name='FotosSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True, verbose_name='Nombre Imagen')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='')),
                ('visible', models.BooleanField(default=False)),
                ('fecha_hora_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de Creación')),
                ('fecha_hora_modificacion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha y Hora de Modificación')),
                ('usuario_creacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UsercreacionFotosSlider', to=settings.AUTH_USER_MODEL)),
                ('usuario_modificacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='UserModFotosSlider', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Fotos Slider',
                'verbose_name_plural': 'Fotos Slider',
            },
        ),
    ]
