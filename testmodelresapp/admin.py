from django.contrib import admin
from .models import Faculty, Department, Student, ResearchScholar, JournalArticle, ConferenceArticle, BookSeries, Project
# Register your models here.

admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Student)
admin.site.register(ResearchScholar)
admin.site.register(JournalArticle)
admin.site.register(ConferenceArticle)
admin.site.register(BookSeries)
admin.site.register(Project)
