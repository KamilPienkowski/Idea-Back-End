# Generated by Django 5.0.4 on 2024-04-14 18:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzdrowisko', '0003_alter_uzdrowisko_address_alter_uzdrowisko_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uzdrowisko',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='uzdrowisko',
            name='image',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='uzdrowisko',
            name='link',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='uzdrowisko',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='uzdrowisko',
            name='phoneNumber',
            field=models.CharField(max_length=15),
        ),
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='opinions', to='uzdrowisko.uzdrowisko')),
            ],
        ),
    ]