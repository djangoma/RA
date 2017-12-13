from django.contrib.auth.models import User
from .models import Faculty, Student, ResearchScholar, JournalArticle, ConferenceArticle, Project	
import django_filters

class FacultyFilter(django_filters.FilterSet):
	facultyname = django_filters.CharFilter(lookup_expr="icontains")
	class Meta:
		model = Faculty
		fields = ['facultyname','deptname']

class StudentFilter(django_filters.FilterSet):
	sname = django_filters.CharFilter(lookup_expr="icontains")
	class Meta:
		model = Student
		fields = ['sname', 'sregno', 'studentcategory']

class ResearchScholarFilter(django_filters.FilterSet):
	rsname = django_filters.CharFilter(lookup_expr="icontains")
	class Meta:
		model = ResearchScholar
		fields = ['rsname', 'rsregno', 'rssupervisor',]
		
class JournalArticleFilter(django_filters.FilterSet):
	jpublishedon__month__gte = django_filters.NumberFilter(name='jpublishedon', lookup_expr='month__gte')
	jpublishedon__year__gte = django_filters.NumberFilter(name='jpublishedon', lookup_expr='year__gte')
	jpublishedon__month__lte = django_filters.NumberFilter(name='jpublishedon', lookup_expr='month__lte')
	jpublishedon__year__lte = django_filters.NumberFilter(name='jpublishedon', lookup_expr='year__lte')
	class Meta:
		model = JournalArticle
		fields = ['jpublishedon__year__gte','jpublishedon__month__gte','jpublishedon__year__lte','jpublishedon__month__lte','jstatus','pubfromconf','facultyauthor','studentauthor','rsauthor','jtr','jsjr','jsnip','jissn',]
		
		

	