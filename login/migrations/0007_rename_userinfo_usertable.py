# Generated by Django 5.0.4 on 2024-04-30 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_alter_userinfo_email_alter_userinfo_password_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='userInfo',
            new_name='usertable',
        ),
    ]