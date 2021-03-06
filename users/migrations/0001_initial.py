# Generated by Django 4.0.3 on 2022-03-26 19:48

from django.db import migrations, models
import django.db.models.deletion
import users.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id_user', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('password', models.CharField(max_length=120)),
                ('profile_picture', models.ImageField(upload_to=users.models.upload_profile_picture)),
                ('country', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('join_date', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='products.product')),
            ],
        ),
    ]
