# Generated by Django 4.1.1 on 2022-09-10 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0006_alter_books_bookpdf'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='bookPdf',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]