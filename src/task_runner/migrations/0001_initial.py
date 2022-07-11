import django.core.validators
from django.db import migrations, models
from django.contrib.auth.models import User


def add_default_admin(apps, schema_editor):
    User.objects.create_superuser(username='admin', password='admin')


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('input', models.IntegerField(validators=[django.core.validators.MinValueValidator(100000), django.core.validators.MaxValueValidator(99999999)])),
                ('result', models.CharField(default='', max_length=256)),
            ],
        ),
        migrations.RunPython(add_default_admin)
    ]
