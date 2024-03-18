# Generated by Django 5.0.3 on 2024-03-18 22:39

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_loan'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='loan',
            name='reader',
        ),
        migrations.AddField(
            model_name='loan',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='book_reader', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
