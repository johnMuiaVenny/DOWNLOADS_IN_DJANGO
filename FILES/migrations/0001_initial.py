# Generated by Django 3.2.6 on 2021-08-29 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MYFILES',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=255)),
                ('File', models.FileField(upload_to='Files')),
                ('Cover', models.FileField(upload_to='Covers')),
            ],
        ),
    ]
