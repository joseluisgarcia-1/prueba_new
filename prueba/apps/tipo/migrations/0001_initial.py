# Generated by Django 2.1.11 on 2019-10-13 02:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Descripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=500000000)),
            ],
        ),
        migrations.CreateModel(
            name='Receta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tipo.Descripcion')),
            ],
        ),
    ]
