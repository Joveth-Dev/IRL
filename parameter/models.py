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
    ACTIVE = 'A'
    INACTIVE = 'I'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]
    person = models.OneToOneField(Person, on_delete=models.CASCADE)
    designation = models.CharField(max_length=50)
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
    researcher = models.ManyToManyField(Researcher)
    title = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    date_started = models.DateField()
    date_ended = models.DateField()
    duration = models.SmallIntegerField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Researches'


class Project(models.Model):
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
    date_ended = models.DateField()
    duration = models.SmallIntegerField()

    def __str__(self) -> str:
        return self.title
