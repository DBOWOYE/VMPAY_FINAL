# Generated by Django 3.2.4 on 2023-07-21 08:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('number_card', '0001_initial'),
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VmpayAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('accurency', models.CharField(default='GNF', max_length=3)),
                ('customer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
                ('number_card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='number_card.numbercard')),
            ],
        ),
    ]
