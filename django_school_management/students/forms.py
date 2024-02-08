from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.bootstrap import Tab, TabHolder
from crispy_forms.layout import (
    Layout, Field, ButtonHolder, Submit
)
from .models import AdmissionStudent, CounselingComment, Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = AdmissionStudent
        fields = [
            'name',
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
            'current_address',
            'permanent_address',
            'mobile_number',
            'guardian_mobile_number',
            'email',
            'department_choice',
            'exam_name',
            'highest_qualification',
            'passing_year',
            'course_name',
            'other_qualification',
            'explaination_education',
            'date_papitaiso_kina',
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
        ]
        widgets = {
            'date_of_birth': forms.TextInput({'type': 'date'}),
        }


class AdmissionForm(forms.ModelForm):
    class Meta:
        model = AdmissionStudent
        fields = [
            'choosen_department',
        ]


class StudentRegistrantUpdateForm(forms.ModelForm):
    class Meta:
        model = AdmissionStudent
        fields = [
            'name',
            'photo',
            'fathers_name',
            'mothers_name',
            'date_of_birth',
            'current_address',
            'permanent_address',
            'mobile_number',
            'email',
            'choosen_department',
            'admitted',
            'paid',
            'rejected',
        ]
        widgets = {
            'date_of_birth': forms.TextInput({'type': 'date'}),
        }


class CounselingDataForm(forms.ModelForm):
    class Meta:
        model = CounselingComment
        fields = ['comment', ]


class StudentUpdateForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = (
            'roll',
            'registration_number',
            'semester',
            'guardian_mobile',
            'is_alumni', 'is_dropped'
        )
