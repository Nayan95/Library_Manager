# Generated by Django 4.1.1 on 2022-09-10 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Management', '0004_alter_books_bookid'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='bookPdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]