# Generated by Django 5.1.2 on 2024-10-28 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DailyMission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mission_text', models.CharField(max_length=255)),
                ('last_updated', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
