# Generated by Django 2.2.3 on 2020-02-20 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chairman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chairman_name', models.CharField(blank=True, max_length=200, null=True)),
                ('specialization', models.CharField(blank=True, max_length=200, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('document', models.FileField(upload_to='chairman/')),
            ],
        ),
    ]