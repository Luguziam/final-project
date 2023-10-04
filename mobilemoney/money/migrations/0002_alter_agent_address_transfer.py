# Generated by Django 4.2.5 on 2023-09-29 09:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('money', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='address',
            field=models.CharField(blank=True, default='none', max_length=60, null=True),
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transfer_rate', models.IntegerField()),
                ('amount_transfered', models.IntegerField()),
                ('transfer_date', models.DateField()),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='money.agent')),
            ],
        ),
    ]
