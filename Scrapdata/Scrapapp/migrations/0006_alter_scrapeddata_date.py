# Generated by Django 4.2.5 on 2023-09-09 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Scrapapp', '0005_alter_scrapeddata_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scrapeddata',
            name='date',
            field=models.CharField(default=True, max_length=100),
        ),
    ]
