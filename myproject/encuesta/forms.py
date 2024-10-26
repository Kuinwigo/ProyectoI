# encuesta/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SurveyResponse, Photo, Video
from django.forms import modelformset_factory

# Formulario de Registro
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

# Formulario de Encuesta
class SurveyResponseForm(forms.ModelForm):
    clause_1 = forms.BooleanField(label="Estoy de acuerdo en que los materiales enviados sean compartidos públicamente.", required=True)
    clause_2 = forms.BooleanField(label="Confirmo que las imágenes enviadas son contenido apropiado y relevante.", required=True)
    clause_3 = forms.BooleanField(label="Acepto no enviar contenido no solicitado.", required=True)
    clause_4 = forms.BooleanField(label="Doy mi consentimiento para el uso de las imágenes en proyectos de la biblioteca.", required=True)
    clause_5 = forms.BooleanField(label="Comprendo que los archivos enviados serán revisados antes de ser aceptados.", required=True)

    class Meta:
        model = SurveyResponse
        fields = ['comments']

# FormSets para fotos y videos
PhotoFormSet = modelformset_factory(Photo, form=forms.ModelForm, fields=('image', 'description'), extra=1, can_delete=True)
VideoFormSet = modelformset_factory(Video, form=forms.ModelForm, fields=('file', 'description'), extra=1, can_delete=True)
