# Generated by Django 5.0.4 on 2024-04-11 19:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uzdrowisko', '0002_alter_uzdrowisko_address_alter_uzdrowisko_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uzdrowisko',
            name='address',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Name can only contain Polish characters and spaces', regex='^[[a-zA-Z0-9_\\-ąćęłńóśźżĄĆĘŁŃÓŚŹŻ.,:;/@&=?+%$#!*(){}\'" ]]+$')]),
        ),
        migrations.AlterField(
            model_name='uzdrowisko',
            name='image',
            field=models.CharField(max_length=500, validators=[django.core.validators.RegexValidator(message='Name can only contain Polish characters and spaces', regex='^[[a-zA-Z0-9_\\-ąćęłńóśźżĄĆĘŁŃÓŚŹŻ.,:;/@&=?+%$#!*(){}\'" ]]+$')]),
        ),
        migrations.AlterField(
            model_name='uzdrowisko',
            name='link',
            field=models.CharField(max_length=500, validators=[django.core.validators.RegexValidator(message='Name can only contain Polish characters and spaces', regex='^[[a-zA-Z0-9_\\-ąćęłńóśźżĄĆĘŁŃÓŚŹŻ.,:;/@&=?+%$#!*(){}\'" ]]+$')]),
        ),
        migrations.AlterField(
            model_name='uzdrowisko',
            name='name',
            field=models.CharField(max_length=100, validators=[django.core.validators.RegexValidator(message='Name can only contain Polish characters and spaces', regex='^[[a-zA-Z0-9_\\-ąćęłńóśźżĄĆĘŁŃÓŚŹŻ.,:;/@&=?+%$#!*(){}\'" ]]+$')]),
        ),
        migrations.AlterField(
            model_name='uzdrowisko',
            name='phoneNumber',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(message='Name can only contain Polish characters and spaces', regex='^[[a-zA-Z0-9_\\-ąćęłńóśźżĄĆĘŁŃÓŚŹŻ.,:;/@&=?+%$#!*(){}\'" ]]+$')]),
        ),
    ]
