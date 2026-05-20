from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('back-end', 'back-end'), ('front-end', 'front-end'), ('ios', 'iOS'), ('android', 'Android')], max_length=10)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True, max_length=2048)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, max_length=2048)),
                ('priority', models.CharField(choices=[('low', 'LOW'), ('medium', 'MEDIUM'), ('high', 'HIGH')], max_length=10)),
                ('balise', models.CharField(choices=[('bug', 'BUG'), ('feature', 'FEATURE'), ('task', 'TASK')], max_length=10)),
                ('status', models.CharField(choices=[('to-do', 'To Do'), ('in-progress', 'In Progress'), ('finished', 'Finished')], default='to-do', max_length=15)),
                ('assign_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_issue', to=settings.AUTH_USER_MODEL)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issue', to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.project')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True, max_length=2048)),
                ('uuid', models.TextField(blank=True, default='f491101c-6800-41ab-96a7-12a546a94e09', max_length=2048)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='support.issue')),
            ],
        ),
    ]
