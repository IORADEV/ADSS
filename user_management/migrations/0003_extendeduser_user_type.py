# Generated by Django 2.2 on 2020-01-21 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_management', '0002_auto_20191220_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='extendeduser',
            name='user_type',
            field=models.CharField(choices=[('AN', 'anonymous'), ('FR', 'forestry'), ('NR', 'nursery')], default=1, max_length=10),
        ),
    ]