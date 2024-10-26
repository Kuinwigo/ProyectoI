# encuesta/models.py
from django.db import models

class SurveyResponse(models.Model):
    comments = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Response #{self.id}"

class Photo(models.Model):
    survey_response = models.ForeignKey(SurveyResponse, related_name='photos', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/')
    description = models.CharField(max_length=255, blank=True, null=True, help_text="Descripción de la foto")

    def __str__(self):
        return f"Photo for Response #{self.survey_response.id}"

class Video(models.Model):
    survey_response = models.ForeignKey(SurveyResponse, related_name='videos', on_delete=models.CASCADE)
    file = models.FileField(upload_to='videos/')
    description = models.CharField(max_length=255, blank=True, null=True, help_text="Descripción del video")

    def __str__(self):
        return f"Video for Response #{self.survey_response.id}"
