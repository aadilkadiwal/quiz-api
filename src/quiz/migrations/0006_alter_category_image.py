# Generated by Django 4.0.3 on 2022-05-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0005_alter_category_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='defaultcategory.jpg', upload_to='category'),
        ),
    ]
