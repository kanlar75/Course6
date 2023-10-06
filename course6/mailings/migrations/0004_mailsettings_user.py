# Generated by Django 4.2.5 on 2023-09-20 10:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mailings', '0003_remove_message_mailing_remove_message_user_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailsettings',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='create_mail', to=settings.AUTH_USER_MODEL, verbose_name='добавил рассылку'),
        ),
    ]