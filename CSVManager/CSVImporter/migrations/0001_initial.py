# Generated by Django 4.2.5 on 2023-10-02 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CsvFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='File name')),
                ('csv_file', models.ImageField(upload_to='files/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'CsvFile',
                'verbose_name_plural': 'CsvFiles',
                'db_table': 'csv_file',
                'ordering': ['created'],
            },
        ),
    ]
