# Generated by Django 2.0.6 on 2019-09-24 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise1App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('realName', models.CharField(max_length=200)),
                ('accountNumber', models.IntegerField(default=0)),
                ('balance', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
        ),
    ]
