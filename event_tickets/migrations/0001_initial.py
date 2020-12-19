# Generated by Django 3.1.4 on 2020-12-19 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.IntegerField(choices=[(0, 'Regular'), (1, 'Premium'), (2, 'VIP')])),
                ('start_time', models.DateTimeField(auto_now=True)),
                ('duration', models.IntegerField(default=15)),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=32)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_type', models.IntegerField(choices=[(0, 'Regular'), (1, 'Premium'), (2, 'VIP')], default=0)),
                ('quantity', models.IntegerField(default=0)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
            options={
                'unique_together': {('event', 'ticket_type')},
            },
        ),
    ]