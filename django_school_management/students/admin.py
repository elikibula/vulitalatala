from django.contrib import admin
from .models import Student, AdmissionStudent, RegularStudent


class AdmissionStudentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'created', 
        'department_choice', 'admitted',
        'assigned_as_student'
    )
    list_editable = ('admitted', 'assigned_as_student')
    fieldsets = (
        ('Personal Infor', {
            'fields': ('name',
            'fathers_name',
            'mothers_name',
            'date_of_birth',
            'gender',
            'yasana',
            'tikina',
            'koro',
            'date_married',
            'spouse_name',
            'spouse_job',
            'children_name',
            )
        }),
       ('Contact Infor', {
            'fields': ('current_address',
            'permanent_address',
            'mobile_number',
            'guardian_mobile_number',
            'email',
            )
        }),
        ('Education Infor', {
            'fields': ('exam_name',
            'highest_qualification',
            'passing_year',
            'course_name',
            'other_qualification',
            'explaination_education',
            )
        }),
         ('Veiqaravi Infor', {
            'fields': ('date_papitaiso_kina',
            'date_sigadina_kina',
            'yabaki_tabaki_kina',
            'tavi_qaravi_nikua',
            'yabaki_tekivu_kina',
            'nona_tukutuku_tavi_vakai_talatala',
            'nona_wasewase',
            'nona_tabacakacaka',
            'nona_tubu_ni_veiqaravi',
            'nona_tukutuku_ni_cakacaka',
            'vakamacala_tale_eso',
            )
        }),
    )



class StudentAdmin(admin.ModelAdmin):
    list_display = ('admission_student',
                    'ac_session',
                    'batch',
                    'temp_serial',
                    'temporary_id')

    

admin.site.register(Student, StudentAdmin)
admin.site.register(AdmissionStudent, AdmissionStudentAdmin)
admin.site.register(RegularStudent)
