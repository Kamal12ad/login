# Generated by Django 5.0.4 on 2024-04-28 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_alter_userinfo_email_alter_userinfo_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='Email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='Username',
            field=models.CharField(max_length=50),
        ),
    ]