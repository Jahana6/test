# Generated by Django 4.1.6 on 2023-02-05 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('pub_date', models.DateField(auto_now=True)),
                ('count_pages', models.IntegerField()),
            ],
        ),
    ]
