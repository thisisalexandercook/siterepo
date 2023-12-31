# Generated by Django 4.2 on 2023-05-03 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [migrations.swappable_dependency(settings.AUTH_USER_MODEL)]

    operations = [
        migrations.CreateModel(
            name="Room",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("room_name", models.CharField(max_length=50)),
                ("photo", models.ImageField(upload_to="")),
                ("price", models.IntegerField()),
                ("available", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("fname", models.CharField(max_length=50)),
                ("lname", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=10)),
                ("Address", models.TextField()),
                ("persons", models.IntegerField()),
                ("child", models.IntegerField()),
                ("a_date", models.CharField(max_length=10)),
                ("d_date", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=254)),
                (
                    "room",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Club.room"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
