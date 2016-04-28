from django.contrib import admin

# Register your models here.
from graduates.models import Graduate, Speciality, Faculty, Kaf


class GraduateAdmin(admin.ModelAdmin):
    list_filter = ['graduate_surname',
                   ]
    search_fields = ['graduate_surname',
                     ]

admin.site.register(Graduate, GraduateAdmin)


class SpecialityAdmin(admin.ModelAdmin):
    list_filter = ['speciality_name',
                   ]
    search_fields = ['speciality_name',
                     ]

admin.site.register(Speciality, SpecialityAdmin)


class FacultyAdmin(admin.ModelAdmin):
    list_filter = ['faculty_name',
                   ]
    search_fields = ['faculty_name',
                     ]

admin.site.register(Faculty, FacultyAdmin)


class KafAdmin(admin.ModelAdmin):
    list_filter = ['kaf_name',
                   ]
    search_fields = ['kaf_name',
                     ]

admin.site.register(Kaf, KafAdmin)
