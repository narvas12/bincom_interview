# Generated by Django 3.2.18 on 2023-05-27 02:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnnouncedPuResults',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polling_unit_uniqueid', models.PositiveIntegerField()),
                ('party_abbreviation', models.CharField(max_length=10)),
                ('party_score', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Lga',
            fields=[
                ('lga_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('lga_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('state_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('state_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ward',
            fields=[
                ('ward_id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('ward_name', models.CharField(max_length=255)),
                ('lga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pollingunit.lga')),
            ],
        ),
        migrations.CreateModel(
            name='PollingUnit',
            fields=[
                ('uniqueid', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('polling_unit_id', models.PositiveIntegerField()),
                ('polling_unit_number', models.CharField(max_length=255)),
                ('polling_unit_name', models.CharField(max_length=255)),
                ('polling_unit_description', models.TextField(blank=True, null=True)),
                ('lat', models.DecimalField(decimal_places=8, max_digits=10)),
                ('long', models.DecimalField(decimal_places=8, max_digits=11)),
                ('entered_by_user', models.CharField(blank=True, max_length=255, null=True)),
                ('date_entered', models.DateField(blank=True, null=True)),
                ('user_ip_address', models.GenericIPAddressField(blank=True, null=True)),
                ('lga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pollingunit.lga')),
                ('ward', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pollingunit.ward')),
            ],
        ),
        migrations.AddField(
            model_name='lga',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pollingunit.state'),
        ),
    ]