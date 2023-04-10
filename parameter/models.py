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


class Coordinator(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    SEX_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    name = models.CharField(max_length=255)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    agency_or_address = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name


class Program(models.Model):
    coordinator = models.ForeignKey(
        Coordinator, on_delete=models.CASCADE, related_name='programs')
    title = models.CharField(max_length=255)
    executive_summary = models.TextField()
    is_posted = models.BooleanField(default=False)
    date_posted = models.DateField(
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.title


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
    date_started = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return self.person.get_full_name()

    class Meta:
        verbose_name = 'SALOG Employee'
        verbose_name_plural = 'SALOG Employees'


class Project(models.Model):
    ONGOING = 'O'
    INACTIVE = 'I'
    STATUS_CHOICES = [
        (ONGOING, 'Ongoing'),
        (INACTIVE, 'Inactive'),
    ]
    program = models.ForeignKey(
        Program,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    SALOG_employees = models.ManyToManyField(
        SALOG_Employee, related_name='projects')
    title = models.CharField(max_length=250)
    project_description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    date_started = models.DateField()
    date_ended = models.DateField(blank=True, null=True)
    duration = models.SmallIntegerField()
    is_posted = models.BooleanField(default=False)
    date_posted = models.DateField(
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.title


class LinkagePartner(models.Model):
    ACTIVE = 'A'
    INACTIVE = 'I'
    STATUS_CHOICES = [
        (ACTIVE, 'Active'),
        (INACTIVE, 'Inactive'),
    ]
    name = models.CharField(max_length=250)
    description = models.TextField()
    logo = models.ImageField(upload_to='parameter/linkage_partners/image')
    date_of_linkage = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Linkage Partner'
        verbose_name_plural = 'Linkage Partners'


class Equipment(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='parameter/equipment/image')

    def __str__(self) -> str:
        return self.name


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
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    linkage_partners = models.ManyToManyField(
        LinkagePartner, related_name='linkage_researches')
    researchers = models.ManyToManyField(Researcher, related_name='researches')
    equipments = models.ManyToManyField(Equipment, 'equipment_researches')
    title = models.CharField(max_length=250)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    date_started = models.DateField()
    date_ended = models.DateField(blank=True, null=True)
    duration = models.SmallIntegerField()
    is_posted = models.BooleanField(default=False)
    date_posted = models.DateField(
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Researches'
