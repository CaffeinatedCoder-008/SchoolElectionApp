# Generated by Django 5.1.1 on 2025-03-22 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voteApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='candidate_images/'),
        ),
    ]
