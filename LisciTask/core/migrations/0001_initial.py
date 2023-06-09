# Generated by Django 4.2.1 on 2023-06-01 12:29

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name="LearningActivity",
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
                ("name", models.CharField(max_length=255)),
                ("completed", models.BooleanField(default=False)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="learning_activities",
                        to="core.course",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UserData",
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
                ("timestamp", models.DateTimeField(auto_now=True)),
                ("data", models.TextField()),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("COMPLETED", "Completed"),
                            ("NOT_COMPLETED", "Not Completed"),
                        ],
                        default="",
                        max_length=100,
                    ),
                ),
                ("completed_at", models.DateTimeField(null=True)),
                (
                    "progress",
                    models.DecimalField(decimal_places=1, max_digits=4, null=True),
                ),
                (
                    "score",
                    models.DecimalField(decimal_places=1, max_digits=6, null=True),
                ),
                ("manually_finished", models.BooleanField(default=False, null=True)),
                ("manually_finished_at", models.DateTimeField(blank=True, null=True)),
                (
                    "learn_unit",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="course_user_data",
                        to="core.course",
                    ),
                ),
                (
                    "learning_activity",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="element_user_progress",
                        to="core.learningactivity",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="user_data",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "User Tracking Data",
                "ordering": ["-timestamp"],
            },
        ),
    ]
