from model_utils.models import TimeStampedModel

from django.db import (
    models, OperationalError, 
    IntegrityError, transaction
)
from django.conf import settings
from django_school_management.academics.models import (
    Department, Semester,
    AcademicSession, Batch, 
    TempSerialID
)
from django_school_management.teachers.models import Teacher
from .utils import model_help_texts

gender_Choice = (
    ("male", "Male"),
    ("female", "Female")
)

yasana_Choice = (
    ("ba", "Ba"),
    ("bua", "Bua"),
    ("cakaudrove", "Cakaudrove"),
    ("kadavu", "Kadavu"),
    ("lau", "Lau"),
    ("lomaiviti", "Lomaiviti"),
    ("macuata", "Macuata"),
    ("nadroga/navosa", "Nadroga/Navosa"),
    ("naitasiri", "Naitasiri"),
    ("namosi", "Namosi"),
    ("ra", "Ra"),
    ("rewa", "Rewa"),
    ("serua", "Serua"),
    ("tailevu", "Tailevu"),
)

hq_Choice = (
        ('PHD', 'Doctor'),
        ('MST', 'Masters'),
        ('DGR', 'Degree'),
        ('DIP', 'Diploma'),
        ('CER', 'Certificate'),
        ('F7', 'Form 7'),
        ('F6', 'Form 6'),
        ('OTH', 'Others'),
    )

tavi_Choice = (
    ("talcg", "Talatala Vakacegu"),
    ("tlqs", "Talatala Qase"),
    ("talyc","Talatala Yaco"),
    ("taltv","Talatala Vakatovolei"),
)

class StudentManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_alumni=False,
            is_dropped=False
        )


class AlumniManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(
            is_alumni=True
        )


class StudentBase(TimeStampedModel):
    id = models.AutoField(primary_key=True)
    name = models.CharField(model_help_texts.STUDENT_BASE_NAME, max_length=100, help_text='Full name on Birth Certificate')
    photo = models.ImageField(upload_to='students/applicant/')
    fathers_name = models.CharField(model_help_texts.STUDENT_BASE_FATHER_NAME, max_length=100, help_text='Full name on Birth Certificate')
    mothers_name = models.CharField(model_help_texts.STUDENT_BASE_MOTHER_NAME, max_length=100, help_text='Full name on Birth Certificate')
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=gender_Choice,max_length=50, blank=True)
    yasana = models.CharField(choices=yasana_Choice, max_length=50, blank=True, null=True,)
    tikina = models.CharField(max_length=255, null=True, blank=True,)
    koro = models.CharField(max_length=255, null=True, blank=True,)
    date_married = models.DateField(null=True, max_length=50, blank=True, help_text='Na siga e vakamau kina - Dd/Mm/Yy eg 23/03/2010')
    spouse_name = models.CharField(max_length=255, blank=True, null=True, help_text='Na yacana kece mai nai vola ni sucu')
    spouse_job = models.CharField(max_length=255, blank=True, help_text='Na nona cakacaka ko Watina')
    children_name = models.TextField(max_length=255, blank=True, null=True, help_text='Na yacadra kece mai nai vola ni sucu kei na yabaki ra sucu kina')
    email = models.EmailField()
    current_address = models.TextField()
    permanent_address = models.TextField()
    mobile_number = models.CharField(max_length=11)
    guardian_mobile_number = models.CharField(max_length=11)    
    department_choice = models.ForeignKey(
        Department,
        on_delete=models.CASCADE
    )
    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class CounselingComment(TimeStampedModel):
    counselor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, null=True
    )
    registrant_student = models.ForeignKey(
        'AdmissionStudent',
        on_delete=models.CASCADE, null=True
    )
    comment = models.CharField(max_length=150)

    def __str__(self):
        date = self.created.strftime("%d %B %Y")
        return self.comment
    
    class Meta:
        ordering = ['-created', ]


class AdmissionStudent(StudentBase):
    APPLICATION_TYPE_CHOICE = (
        ('1', 'Online'),
        ('2', 'Offline')
    )
    EXAM_NAMES = (
        ('BED', 'BED Degree In Theology'),
        ('DIP', 'Diploma In Theology'),
    )
    
    counseling_by = models.ForeignKey(
        Teacher, related_name='counselors',
        on_delete=models.CASCADE, null=True
    )
    counsel_comment = models.ManyToManyField(
        CounselingComment, blank=True
    )
    choosen_department = models.ForeignKey(
        Department, related_name='admission_students',
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    exam_name = models.CharField(
        choices=EXAM_NAMES,
        max_length=10
    )
    highest_qualification = models.CharField(choices=hq_Choice, max_length=50,null=True)
    passing_year = models.CharField(max_length=4)
    course_name = models.TextField(blank=True, help_text='Na vuli e qaravi tiko kei na yabaki me oti kina')
    other_qualification = models.TextField(blank=True, help_text='Na vuli tale eso e rawati kei na yabaki')
    explaination_education = models.TextField(blank=True)
    date_papitaiso_kina = models.DateField(null=True, max_length=50, blank=True, help_text='Na tikini siga ka Papitaiso kina/ ke kilai ga na yabaki ia me vaka na 01/01/2002 e vakaraitaka ni yabaki 2002')
    date_sigadina_kina = models.DateField(null=True, max_length=50, blank=True, help_text='Na tikini siga ka Siga Dina kina/ ke kilai ga na yabaki ia me vaka na 01/01/2002 e vakaraitaka ni yabaki 2002')
    yabaki_tabaki_kina = models.DateField(null=True, max_length=50, blank=True, help_text='Na tikini siga ka Tabaki kina')
    tavi_qaravi_nikua = models.CharField(choices=tavi_Choice, max_length=50, blank=True, help_text='Nai tavi vakai talatala ka qarava tiko ena gauna nikua')
    yabaki_tekivu_kina = models.CharField(max_length=255, blank=True, help_text='Na yabaki ka tekivu kacivi kina me qarava nai tavi vakai Talatala ka taura tiko nikua')
    nona_tukutuku_tavi_vakai_talatala = models.TextField(blank=True, help_text='Na nona i tukutuku ena vuku ni nona i tavi vakai Talatala')
    nona_wasewase = models.TextField(blank=True, help_text='Na nona i tukutuku ena vuku ni nona i tavi vakai Talatala')
    nona_tabacakacaka = models.TextField(blank=True, help_text='Na nona i tukutuku ena vuku ni nona i tavi vakai Talatala')
    nona_tubu_ni_veiqaravi = models.TextField(blank=True,help_text='Nona record ni veiqaravi vakai wiliwili ni vavakoso')
    nona_tukutuku_ni_cakacaka = models.TextField(blank=True, help_text='Na nona i tukutuku ena vuku ni nona cakacaka')
    vakamacala_tale_eso = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    admitted = models.BooleanField(default=False)
    admission_date = models.DateField(blank=True, null=True)
    paid = models.BooleanField(default=False)
    application_type = models.CharField(
        max_length=1,
        choices=APPLICATION_TYPE_CHOICE,
        default='1'
    )
    migration_status = models.CharField(
        max_length=255,
        blank=True, null=True
    )
    rejected = models.BooleanField(default=False)
    assigned_as_student = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if self.department_choice != self.choosen_department:
            status = f'From {self.department_choice} to {self.choosen_department}'
            self.migration_status = status
            super().save(*args, **kwargs)
        super().save(*args, **kwargs)


class Student(TimeStampedModel):
    admission_student = models.ForeignKey(
        AdmissionStudent,
        on_delete=models.CASCADE
    )
    roll = models.CharField(max_length=6, unique=True, blank=True, null=True)
    registration_number = models.CharField(max_length=6, unique=True, blank=True, null=True)
    temp_serial = models.CharField(max_length=50, blank=True, null=True)
    temporary_id = models.CharField(max_length=50, blank=True, null=True)
    semester = models.ForeignKey(
        Semester, on_delete=models.CASCADE)
    ac_session = models.ForeignKey(
        AcademicSession, on_delete=models.CASCADE,
        blank=True, null=True
    )
    batch = models.ForeignKey(
        Batch, on_delete=models.CASCADE,
        blank=True, null=True, related_name='students'
    )
    guardian_mobile = models.CharField(max_length=11, blank=True, null=True)
    admitted_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL, null=True
    )
    is_alumni = models.BooleanField(default=False)
    is_dropped = models.BooleanField(default=False)

    # Managers
    objects = StudentManager()
    alumnus = AlumniManager()

    class Meta:
        ordering = ['semester', 'roll', 'registration_number']

    def __str__(self):
        return '{} ({}) semester {} dept.'.format(
            self.admission_student.name,
            self.semester,
            self.admission_student.choosen_department
        )

    def _find_last_admitted_student_serial(self):
        # What is the last temp_id for this year, dept?
        item_serial_obj = TempSerialID.objects.filter(
            department=self.admission_student.choosen_department,
            year=self.ac_session,
        ).order_by('serial').last()

        if item_serial_obj:
            # Return last temp_id
            serial_number = item_serial_obj.serial
            return int(serial_number)
        else:
            # If no temp_id object for this year and department found
            # return 0
            return 0
    
    def get_temp_id(self):
        # Get current year (academic) last two digit
        year_digits = str(self.ac_session.year)[-2:]
        # Get batch of student's department
        batch_digits = self.batch.number
        # Get department code
        department_code = self.admission_student.choosen_department.code
        # Get admission serial of student by department
        temp_serial_key = self.temp_serial
        # return something like: 21-15-666-15
        temp_id = f'{year_digits}-{batch_digits}-' \
                    f'{department_code}-{temp_serial_key}'
        return temp_id

def save(self, *args, **kwargs):
    # Check if batch is not None and chosen_dept != batch.dept is same or not.
    if self.batch and self.admission_student.choosen_department != self.batch.department:
        raise OperationalError(
            f'Cannot assign {self.admission_student.choosen_department} '
            f'departments student to {self.batch.department} department.')
    elif self.admission_student.choosen_department == self.batch.department:
        # Set AdmissionStudent assigned_as_student=True
        self.admission_student.assigned_as_student = True
        self.admission_student.save()

    # Create temporary id for student id if temporary_id is not set yet.
    if not self.temp_serial or not self.temporary_id:
        last_temp_id = self._find_last_admitted_student_serial()
        current_temp_id = str(last_temp_id + 1)
        self.temp_serial = current_temp_id
        self.temporary_id = self.get_temp_id()
        super().save(*args, **kwargs)
        try:
            with transaction.atomic():  
                temp_serial_id = TempSerialID.objects.create(
                    student=self,
                    department=self.admission_student.choosen_department,
                    year=self.ac_session,
                    serial=current_temp_id
                )
                temp_serial_id.save()
        except IntegrityError:
            pass
    super().save(*args, **kwargs)


    def delete(self, *args, **kwargs):
        """ Override delete method """
        # If student is deleted, AdmissionStudent.assigned_as_student
        # should be false.
        self.admission_student.assigned_as_student = False
        self.admission_student.save(*args, **kwargs)


class RegularStudent(TimeStampedModel):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE
    )
    semester = models.ForeignKey(
        Semester, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.student.name} {self.semester}"
