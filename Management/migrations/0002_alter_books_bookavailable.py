# Generated by Django 4.1.1 on 2022-09-08 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='bookAvailable',
            field=models.CharField(choices=[('True', 'True'), ('False', 'False')], default='True', max_length=5),
        ),
    ]
