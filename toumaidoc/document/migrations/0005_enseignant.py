# Generated by Django 4.0 on 2022-01-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('document', '0004_remove_document_file_document_image_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
