# Generated by Django 3.0.2 on 2020-06-26 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_old', models.IntegerField()),
                ('price_new', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('book_up', models.CharField(max_length=50)),
                ('book_down', models.CharField(max_length=50)),
            ],
        ),
    ]
