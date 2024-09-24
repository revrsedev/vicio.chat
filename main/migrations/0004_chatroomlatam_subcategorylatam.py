# Generated by Django 5.0.7 on 2024-08-17 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_chatroom_subcategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoomLatam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='chatrooms/')),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoryLatam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='subcategories/')),
                ('url', models.URLField()),
            ],
        ),
    ]
