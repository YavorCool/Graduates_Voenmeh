from django.db import models


# Факультет
class Faculty(models.Model):
    faculty_name = models.CharField(max_length=100, )
    faculty_code = models.CharField(max_length=100, )
    faculty_description = models.TextField()

    class Meta:
        verbose_name = 'Faculty'
        verbose_name_plural = 'Faculties'

    def __str__(self):
        return u'%s' % self.faculty_name

    def __unicode__(self):
        return u'%s' % self.faculty_name


# Кафедра
class Kaf(models.Model):
    kaf_name = models.CharField(max_length=100, )
    kaf_code = models.CharField(max_length=100, )
    kaf_description = models.TextField()
    kaf_site = models.CharField(max_length=100, blank=True)

    kaf_faculty = models.ForeignKey(Faculty)

    def __str__(self):
        return u'%s' % self.kaf_name

    def __unicode__(self):
        return u'%s' % self.kaf_name


# Специальность
class Speciality(models.Model):
    speciality_name = models.CharField(max_length=250, )
    speciality_code = models.CharField(max_length=30, )
    speciality_description = models.TextField()

    speciality_kaf = models.ForeignKey(Kaf)


    class Meta:
        verbose_name = 'Speciality'
        verbose_name_plural = 'Specialities'

    def __str__(self):
        return u'%s' % self.speciality_name

    def __unicode__(self):
        return u'%s' % self.speciality_name


# Описание выпускника
class Graduate(models.Model):

    DEGREES = (('Бакалавр', 'Бакалавр'),
               ('Специалист', 'Специалист'),
               )

    graduate_surname = models.CharField(max_length=100, )         # Фамилия
    graduate_name = models.CharField(max_length=100, )            # Имя
    graduate_patronymic = models.CharField(max_length=100, blank=True, )      # Отчество
    graduate_birthdate = models.DateField()                     # Дата рождения

    graduate_photo = models.ImageField(blank=True, )              # Фотография
    graduate_address = models.TextField(default="", )             # Место проживания
    graduate_workplace = models.CharField(max_length=100, )
    graduate_science_work = models.TextField()
    graduate_diploma_theme = models.CharField(max_length=100, )

    graduate_speciality = models.ForeignKey(Speciality)             # Специальность
    graduate_gradyear = models.CharField(max_length=4, )               #Год выпуска
    graduate_degree = models.CharField(max_length=20, choices=DEGREES, default='Бакалавр', )

    def __str__(self):
        return u'%s' % self.graduate_surname + ' ' + self.graduate_name[0] + '. ' + self.graduate_patronymic[0]

    def __unicode__(self):
        return u'%s' % self.graduate_surname + ' ' + self.graduate_name[0] + '. ' + self.graduate_patronymic[0]
