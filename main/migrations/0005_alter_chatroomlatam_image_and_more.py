# Generated by Django 5.0.7 on 2024-08-17 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_chatroomlatam_subcategorylatam'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroomlatam',
            name='image',
            field=models.ImageField(upload_to='chatroomslatam/'),
        ),
        migrations.AlterField(
            model_name='subcategorylatam',
            name='image',
            field=models.ImageField(upload_to='subcategorieslatam/'),
        ),
    ]
