# Generated by Django 4.2 on 2023-04-10 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('med_aid', models.CharField(max_length=255)),
                ('med_aid_num', models.IntegerField()),
            ],
        ),
    ]
