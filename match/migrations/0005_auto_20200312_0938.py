# Generated by Django 3.0 on 2020-03-12 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0004_delete_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='human',
            name='review',
        ),
        migrations.AddField(
            model_name='review',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='post',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='match.human'),
        ),
    ]
