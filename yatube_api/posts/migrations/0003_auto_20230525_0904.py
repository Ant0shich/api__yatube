# Generated by Django 3.2.16 on 2023-05-25 06:04

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230524_1432'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.UniqueConstraint(fields=('user', 'following'), name='unique_following'),
        ),
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(('following', django.db.models.expressions.F('user')), _negated=True), name='self_following_disallowed'),
        ),
    ]
