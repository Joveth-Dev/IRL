from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50)
    extension_name = models.CharField(max_length=50, blank=True)
    permanent_address = models.TextField()
    current_address = models.TextField()
    municipality = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)

    def get_full_name(self):
        if self.middle_name == '' and self.extension_name == '':
            return f'{self.first_name} {self.last_name}'
        elif self.middle_name == '':
            return f'{self.first_name} {self.last_name} {self.extension_name}'
        elif self.extension_name == '':
            return f'{self.first_name} {self.middle_name[0]}. {self.last_name}'
        return f'{self.first_name} {self.middle_name[0]}. {self.last_name} {self.extension_name}'

    def __str__(self) -> str:
        return self.get_full_name()

    class Meta:
        verbose_name_plural = 'Person'


class SALOG_Employee(models.Model):
    PROGRAM_LEADER = 'Prog. L'
    PROJECT_LEADER = 'Proj. L'
    PROJECT_STAFF = 'Proj. S'
    DESIGNATION_CHOICES = [
        (PROGRAM_LEADER, 'Program Leader'),
        (PROJECT_LEADER, 'Project Leader'),
        (PROJECT_STAFF, 'Project Staff'),
    ]
    ACTIVE = 'A'
    INACTIVE = 'I'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    designation = models.CharField(
        max_length=7, choices=DESIGNATION_CHOICES, blank=True, null=True)
    rank = models.CharField(max_length=50)
    date_started = models.DateField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return self.person.get_full_name()

    class Meta:
        verbose_name = 'SALOG Employee'
        verbose_name_plural = 'SALOG Employees'


class Researcher(models.Model):
    PRIMARY_AUTHOR = 'P'
    SECONDARY_AUTHOR = 'S'
    LEVEL_CHOICES = [
        (PRIMARY_AUTHOR, 'Primary Author'),
        (SECONDARY_AUTHOR, 'Secondary Author'),
    ]
    ACTIVE = 'A'
    INACTIVE = 'I'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]
    SALOG_employee = models.OneToOneField(
        SALOG_Employee, on_delete=models.CASCADE)
    level = models.CharField(max_length=1, choices=LEVEL_CHOICES)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return self.SALOG_employee.person.get_full_name()


class Research(models.Model):
    ONGOING = 'O'
    INACTIVE = 'I'
    STATUS_CHOICES = [
        (ONGOING, 'Ongoing'),
        (INACTIVE, 'Inactive'),
    ]
    title = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    date_started = models.DateField()
    date_ended = models.DateField(blank=True, null=True)
    duration = models.SmallIntegerField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Researches'


class ResearchResearcher(models.Model):
    researcher = models.ForeignKey(Researcher, on_delete=models.CASCADE)
    research = models.ForeignKey(
        Research, on_delete=models.CASCADE, related_name='research_researcher')

    def __str__(self) -> str:
        return self.researcher.SALOG_employee.person.get_full_name()


class Project(models.Model):
    ONGOING = 'O'
    INACTIVE = 'I'
    STATUS_CHOICES = [
        (ONGOING, 'Ongoing'),
        (INACTIVE, 'Inactive'),
    ]
    title = models.CharField(max_length=250)
    project_description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    date_started = models.DateField()
    date_ended = models.DateField(blank=True, null=True)
    duration = models.SmallIntegerField()

    def __str__(self) -> str:
        return self.title


class ProjectEmployee(models.Model):
    employee = models.ForeignKey(SALOG_Employee, on_delete=models.CASCADE)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name='project_employee')

    def __str__(self):
        return self.employee.person.get_full_name()


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
    duration = models.SmallIntegerField()
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
        (REGIONAL, 'Regional'),
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
    date_posted = models.DateTimeField(auto_now_add=True)
    date_expired = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STAUS_CHOICES)
    # batchfile_id (dire pa sure kun nano gud ine)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'News'
