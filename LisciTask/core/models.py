from django.conf import settings
from django.db import models
from .utils import STATUS


class Course(models.Model):
    name = models.CharField(max_length=255)


class LearningActivity(models.Model):
    name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
    course = models.ForeignKey(Course, related_name="learning_activities", on_delete=models.CASCADE)


class UserData(models.Model):
    timestamp = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_data', on_delete=models.CASCADE)
    learn_unit = models.ForeignKey(
        Course,
        related_name='course_user_data',
        on_delete=models.CASCADE,
        null=True
    )
    learning_activity = models.ForeignKey(
        LearningActivity,
        related_name='element_user_progress',
        on_delete=models.SET_NULL,
        null=True
    )
    data = models.TextField()
    status = models.CharField(max_length=100, default='', blank=True, choices=STATUS.choices)
    completed_at = models.DateTimeField(null=True)
    progress = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    score = models.DecimalField(max_digits=6, decimal_places=1, null=True)
    manually_finished = models.BooleanField(default=False, null=True)
    manually_finished_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name_plural = 'User Tracking Data'
        ordering = ['-timestamp']

    def __str__(self):
        return '%s progress data' % self.user.email

    def mark_course_as_completed(self):
        progress = UserData.objects.filter(
            learning_activity_id=self.learning_activity_id,
            user_id=self.user.id
        ).last()
        # this usually doesn't happen but just in case:
        if not progress:
            UserData.objects.create(
                learning_activity_id=self.learning_activity_id,
                user_id=self.user.id,
                status=STATUS.COMPLETED
            )
        else:
            # if not already finished, finish now!
            if progress.status != STATUS.COMPLETED:
                progress.status = STATUS.COMPLETED
                progress.save()
