# Generated by Django 3.2.5 on 2021-07-21 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=50000)),
                ('email', models.CharField(max_length=200)),
                ('Contact_No', models.IntegerField(max_length=12)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='Large_price',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='Medium_price',
            field=models.FloatField(null=True),
        ),
    ]