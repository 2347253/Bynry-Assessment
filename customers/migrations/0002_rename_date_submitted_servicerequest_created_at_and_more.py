# Generated by Django 4.2.5 on 2025-01-21 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servicerequest',
            old_name='date_submitted',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='servicerequest',
            name='date_resolved',
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='attachment',
            field=models.FileField(blank=True, null=True, upload_to='attachments/'),
        ),
        migrations.AddField(
            model_name='servicerequest',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='servicerequest',
            name='request_type',
            field=models.CharField(choices=[('installation', 'Installation'), ('repair', 'Repair'), ('maintenance', 'Maintenance')], max_length=50),
        ),
    ]
