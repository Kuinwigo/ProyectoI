# encuesta/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import SurveyResponse, Photo, Video
from .forms import RegisterForm, SurveyResponseForm, PhotoFormSet, VideoFormSet

# Vista de Registro de Usuario
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('survey_form')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

# Vista del Formulario de Encuesta
@login_required
def survey_form(request):
    if request.method == 'POST':
        survey_form = SurveyResponseForm(request.POST)
        photo_formset = PhotoFormSet(request.POST, request.FILES, queryset=Photo.objects.none())
        video_formset = VideoFormSet(request.POST, request.FILES, queryset=Video.objects.none())

        if survey_form.is_valid() and photo_formset.is_valid() and video_formset.is_valid():
            survey_response = survey_form.save()

            for photo_form in photo_formset:
                if photo_form.cleaned_data:
                    photo = photo_form.save(commit=False)
                    photo.survey_response = survey_response
                    photo.save()

            for video_form in video_formset:
                if video_form.cleaned_data:
                    video = video_form.save(commit=False)
                    video.survey_response = survey_response
                    video.save()

            return redirect('thank_you')
    else:
        survey_form = SurveyResponseForm()
        photo_formset = PhotoFormSet(queryset=Photo.objects.none())
        video_formset = VideoFormSet(queryset=Video.objects.none())

    return render(request, 'survey_form.html', {
        'survey_form': survey_form,
        'photo_formset': photo_formset,
        'video_formset': video_formset
    })

# Vista para la Página de Agradecimiento
@login_required
def thank_you(request):
    return render(request, 'thank_you.html')
