from django.contrib.auth.models import User
from .models import Faculty, Student, ResearchScholar, JournalArticle, ConferenceArticle, Project, BookSeries
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
	jtitle = django_filters.CharFilter(name='jtitle', lookup_expr='icontains')
	jname = django_filters.CharFilter(name='jname', lookup_expr='icontains')
	#jtr__gt = django_filters.NumberFilter(name ='jtr', lookup_expr='__gt')
	#has_tr = django_filters.NumberFilter(name = 'jtr', lookup_expr='__gt')
	has_jtr = django_filters.BooleanFilter(name = 'jtr', lookup_expr='isnull', exclude=True)
	has_jsjr = django_filters.BooleanFilter(name = 'jsjr', lookup_expr='isnull', exclude=True)
	has_jsnip = django_filters.BooleanFilter(name = 'jsnip', lookup_expr='isnull', exclude=True)
	has_jissn = django_filters.BooleanFilter(name = 'jissn', lookup_expr='isnull', exclude=True)
	
	class Meta:
		model = JournalArticle
		fields = ['jpublishedon__year__gte','jpublishedon__month__gte','jpublishedon__year__lte','jpublishedon__month__lte','jstatus','pubfromconf','facultyauthor','studentauthor','rsauthor','jtitle','jname','has_jtr','has_jsjr','has_jsnip','has_jissn',]
		
		
class ConferenceArticleFilter(django_filters.FilterSet):
	cdatefrom__month__gte = django_filters.NumberFilter(name='cdatefrom', lookup_expr='month__gte')
	cdatefrom__year__gte = django_filters.NumberFilter(name='cdatefrom', lookup_expr='year__gte')
	cdatefrom__month__lte = django_filters.NumberFilter(name='cdatefrom', lookup_expr='month__lte')
	cdatefrom__year__lte = django_filters.NumberFilter(name='cdatefrom', lookup_expr='year__lte')
	ctitle = django_filters.CharFilter(name='ctitle', lookup_expr='icontains')
	cname = django_filters.CharFilter(name='cname', lookup_expr='icontains')
	#jtr__gt = django_filters.NumberFilter(name ='jtr', lookup_expr='__gt')
	#has_tr = django_filters.NumberFilter(name = 'jtr', lookup_expr='__gt')
	#has_jsjr = django_filters.BooleanFilter(name = 'jsjr', lookup_expr='isnull', exclude=True)
	#has_jsnip = django_filters.BooleanFilter(name = 'jsnip', lookup_expr='isnull', exclude=True)
	#has_jissn = django_filters.BooleanFilter(name = 'jissn', lookup_expr='isnull', exclude=True)
	
	class Meta:
		model = ConferenceArticle
		fields = ['ctitle', 'cname','cdatefrom__month__gte', 'cdatefrom__year__gte','cdatefrom__month__lte','cdatefrom__year__lte',]

class ProjectFilter(django_filters.FilterSet):
	sanctioneddate__month__gte = django_filters.NumberFilter(name='sanctioneddate', lookup_expr='month__gte')
	sanctioneddate__year__gte = django_filters.NumberFilter(name='sanctioneddate', lookup_expr='year__gte')
	sanctioneddate__month__lte = django_filters.NumberFilter(name='sanctioneddate', lookup_expr='month__lte')
	sanctioneddate__year__lte = django_filters.NumberFilter(name='sanctioneddate', lookup_expr='year__lte')
	class Meta:
		model = Project
		fields = ['sanctioneddate__month__gte', 'sanctioneddate__year__gte','sanctioneddate__month__lte','sanctioneddate__year__lte','projectcategory', 'projectstatus','facultypi','facultycopi','student']
		
class BookSeriesFilter(django_filters.FilterSet):
	class Meta:
		model = BookSeries
		fields = ['facultyauthor','studentauthor','rsauthor','refformat']