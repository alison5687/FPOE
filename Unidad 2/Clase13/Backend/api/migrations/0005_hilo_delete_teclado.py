# Generated by Django 5.0.6 on 2024-06-04 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_teclado_conectividad_alter_teclado_formato_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hilo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hilo', models.TextField(blank=True, max_length=50)),
                ('elasticidad', models.FloatField(blank=True, max_length=5000)),
                ('suavidad', models.FloatField(blank=True, max_length=5000)),
                ('tenacidad', models.FloatField(blank=True, max_length=5000)),
                ('ductilidad', models.FloatField(blank=True, max_length=5000, unique=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Teclado',
        ),
    ]