# Generated by Django 5.0.1 on 2024-02-24 19:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transport', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='login',
            old_name='related_model_a',
            new_name='related_model',
        ),
        migrations.RemoveField(
            model_name='login',
            name='email',
        ),
        migrations.RemoveField(
            model_name='login',
            name='user_name',
        ),
    ]