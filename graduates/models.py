from django.db import models


# Факультет
class Faculty(models.Model):
    faculty_name = models.CharField(max_length=100, )
    faculty_code = models.CharField(max_length=100, )
    faculty_description = models.TextField()

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

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

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'

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
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'

    def __str__(self):
        return u'%s' % self.speciality_name

    def __unicode__(self):
        return u'%s' % self.speciality_name


class Group(models.Model):

    DEGREES = (('Бакалавр', 'Бакалавр'),
               ('Специалист', 'Специалист'),
               )

    group_number = models.CharField(max_length=10)
    group_kaf = models.ForeignKey(Kaf)
    group_faculty = models.ForeignKey(Faculty)
    group_end_year = models.CharField(max_length=4, default='2010')
    group_degree = models.CharField(max_length=20, choices=DEGREES, default='Бакалавр', )
    group_speciality = models.ForeignKey(Speciality)

    def __str__(self):
        return u'%s' % self.group_number

    def __unicode__(self):
        return u'%s' % self.group_number

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Учебные группы'
        ordering = ["group_number"]


# Описание выпускника
class Graduate(models.Model):

    graduate_surname = models.CharField(max_length=100)         # Фамилия
    graduate_name = models.CharField(max_length=100)            # Имя
    graduate_patronymic = models.CharField(max_length=100, blank=True, )      # Отчество
    graduate_birthdate = models.DateField()                     # Дата рождения

    graduate_address = models.TextField(default="", blank=True)             # Место проживания
    graduate_workplace = models.CharField(max_length=100, blank=True)
    graduate_science_work = models.TextField(blank=True)
    graduate_diploma_theme = models.CharField(max_length=100, blank=True)

    graduate_kaf = models.ForeignKey(Kaf)
    graduate_faculty = models.ForeignKey(Faculty)
    graduate_group = models.ForeignKey(Group)

    def __str__(self):
        return u'%s' % self.graduate_surname + ' ' + self.graduate_name[0] + '. ' + self.graduate_patronymic[0]

    def __unicode__(self):
        return u'%s' % self.graduate_surname + ' ' + self.graduate_name[0] + '. ' + self.graduate_patronymic[0]

    class Meta:
        verbose_name = 'Выпускник'
        verbose_name_plural = 'Выпускники'
        ordering = ["graduate_surname"]
