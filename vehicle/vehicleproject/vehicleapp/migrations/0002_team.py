# Generated by Django 4.1.3 on 2022-11-02 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicleapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(max_length=250)),
                ('teamimg', models.ImageField(upload_to='pics')),
                ('teamdesc', models.TextField()),
            ],
        ),
    ]
