# Generated by Django 3.0 on 2020-03-12 09:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('match', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='chatlog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatroom', models.CharField(max_length=211111111111)),
                ('chatlo', models.CharField(max_length=2111111111111)),
            ],
        ),
        migrations.CreateModel(
            name='Chatroomname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=211111111111, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=211111111111)),
                ('realname', models.CharField(max_length=211111111111)),
                ('message', models.CharField(max_length=211111111111)),
                ('star', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=211111111111)),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=211111111111)),
            ],
        ),
        migrations.AlterField(
            model_name='human',
            name='name',
            field=models.CharField(max_length=211111111111),
        ),
        migrations.AlterField(
            model_name='matched',
            name='name',
            field=models.CharField(max_length=211111111111),
        ),
        migrations.AlterField(
            model_name='subject',
            name='name',
            field=models.CharField(max_length=211111111111),
        ),
        migrations.AlterField(
            model_name='wantmatch',
            name='name',
            field=models.CharField(max_length=211111111111),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.png', upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='human',
            name='chatroomname',
            field=models.ManyToManyField(to='match.Chatroomname'),
        ),
        migrations.AddField(
            model_name='human',
            name='review',
            field=models.ManyToManyField(to='match.Review'),
        ),
        migrations.AddField(
            model_name='human',
            name='student',
            field=models.ManyToManyField(to='match.Student'),
        ),
        migrations.AddField(
            model_name='human',
            name='tutor',
            field=models.ManyToManyField(to='match.Tutor'),
        ),
    ]
