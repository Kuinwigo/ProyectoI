from django.test import TestCase
# encuesta/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, SurveyForm

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

@login_required
def survey_form(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST, request.FILES)
        if form.is_valid():
            survey = form.save(commit=False)
            survey.user = request.user
            survey.save()
            return redirect('thank_you')
    else:
        form = SurveyForm()
    return render(request, 'survey_form.html', {'form': form})
