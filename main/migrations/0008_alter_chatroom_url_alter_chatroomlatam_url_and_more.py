# Generated by Django 5.0.7 on 2024-08-20 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_chatroom_updated_at_chatroomlatam_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatroom',
            name='url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='chatroomlatam',
            name='url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='chatroomocio',
            name='url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='homecategory',
            name='link',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='recommendedchatroom',
            name='link',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='subcategorylatam',
            name='url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='subcategoryocio',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
