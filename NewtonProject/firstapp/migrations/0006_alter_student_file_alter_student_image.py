# Generated by Django 4.2.2 on 2023-06-27 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0005_alter_student_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='file',
            field=models.FileField(null=True, upload_to='static/files'),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(null=True, upload_to='static/images'),
        ),
    ]