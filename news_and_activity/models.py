from django.db import models
from parameter.models import Project, Research


class Activity(models.Model):
    CONFERENCE = 'C'
    LECTURE = 'L'
    TRAINING = 'T'
    FORUM = 'F'
    MEETING = 'M'
    ACTIVITY_TYPE_CHOICES = [
        (CONFERENCE, 'Conference'),
        (LECTURE, 'Lecture'),
        (TRAINING, 'Training'),
        (FORUM, 'Forum'),
        (MEETING, 'Meeting'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    research = models.ForeignKey(Research, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    activity_type = models.CharField(
        max_length=1, choices=ACTIVITY_TYPE_CHOICES)
    date_started = models.DateField()
    date_ended = models.DateField()
    duration_in_hours = models.IntegerField()
    is_posted = models.BooleanField(default=False)
    date_posted = models.DateField(
        blank=True,
        null=True,
    )
    # batchfile_id (dire pa sure kun nano gud ine)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Activities'


class News(models.Model):
    LOCAL = 'L'
    REGIONAL = 'R'
    NATIONAL = 'N'
    INTERNATIONAL = 'I'
    CATEGORY_CHOICES = [
        (LOCAL, 'Local'),
        (NATIONAL, 'National'),
        (INTERNATIONAL, 'International'),
    ]
    DISPLAY = 'D'
    HIDDEN = 'H'
    STAUS_CHOICES = [
        (DISPLAY, 'Display'),
        (HIDDEN, 'Hidden'),
    ]
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    research = models.ForeignKey(Research, on_delete=models.CASCADE)
    name = models.TextField()
    details = models.TextField()
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    date_expired = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STAUS_CHOICES)
    is_posted = models.BooleanField(default=False)
    date_posted = models.DateField(
        blank=True,
        null=True,
    )
    # batchfile_id (dire pa sure kun nano gud ine)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'News'
