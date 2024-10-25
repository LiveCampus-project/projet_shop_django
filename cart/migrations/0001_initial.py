# Generated by Django 5.1.2 on 2024-10-25 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_system', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('prix', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_emission', models.DateField()),
                ('total_htc', models.FloatField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factures', to='account.user')),
                ('id_delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factures', to='cart.delivery')),
            ],
        ),
        migrations.CreateModel(
            name='Facture_Articles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('article_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factures', to='shop.articles')),
                ('facture_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='articles', to='cart.facture')),
            ],
        ),
    ]