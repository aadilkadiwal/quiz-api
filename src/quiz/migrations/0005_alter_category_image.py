# Generated by Django 4.0.3 on 2022-05-16 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_category_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='defaultcatgory.jpg', upload_to='category'),
        ),
    ]
