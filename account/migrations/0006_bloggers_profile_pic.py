# Generated by Django 3.2.4 on 2021-07-30 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_alter_bloggers_followersnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloggers',
            name='profile_pic',
            field=models.ImageField(blank=True, default='logo.jpg', null=True, upload_to=''),
        ),
    ]
