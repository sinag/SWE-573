# Generated by Django 2.2.1 on 2019-11-08 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('instance', '0001_initial'),
        ('property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TextField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255)),
                ('instance', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='instance.Instance')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='property.Property')),
            ],
            options={
                'verbose_name': 'textfield',
                'verbose_name_plural': 'textfields',
            },
        ),
    ]
