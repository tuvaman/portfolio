# Generated by Django 3.1.4 on 2021-12-10 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MANFRED', '0006_auto_20211208_2351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skills',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='MANFRED.category'),
        ),
    ]
