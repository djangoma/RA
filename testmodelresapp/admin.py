from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Faculty,Department, Student, ResearchScholar, JournalArticle, ConferenceArticle, BookSeries, Project, Document
# Register your models here.
from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from import_export.admin import ImportExportActionModelAdmin
#from core.models import 
from import_export import resources, fields, widgets

from import_export.widgets import ForeignKeyWidget, ManyToManyWidget

class DepartmentResource(resources.ModelResource):
	class Meta:
		model = Department
		fields = ('deptname','id')

class DepartmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = DepartmentResource
	list_display = ('deptname',)
	
class FacultyResource(resources.ModelResource):
    deptname = fields.Field(column_name='deptname', attribute='deptname', widget= ForeignKeyWidget(Department, 'deptname'))
    class Meta:
        model = Faculty
        fields = ('empid','facultyname', )
        #export_order = ('empid','facultyname', 'deptname')
		
class FacultyAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = FacultyResource
	list_display = ('empid','facultyname', 'deptname',)
	list_filter = ('deptname',)
	
class StudentResource(resources.ModelResource):
	deptname = fields.Field(column_name='deptname', attribute='deptname', widget=ForeignKeyWidget(Department, 'deptname'))
	class Meta:
		model = Student
		fields = ('sregno', 'sname', 'sbranch', 'deptname', 'sbatch', 'studentcategory')
		
		
class StudentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = StudentResource
	list_display = ('sregno','sname','deptname','sbatch','studentcategory',)
	list_filter = ('deptname','sbatch','studentcategory',)
	
class ResearchScholarResource(resources.ModelResource):
	rssupervisor = fields.Field(column_name='rssupervisor', attribute='rssupervisor', widget=ForeignKeyWidget(ResearchScholar, 'facultyname'))
	deptname = fields.Field(column_name='deptname', attribute='deptname', widget=ForeignKeyWidget(Department, 'deptname'))
	class Meta:
		model = ResearchScholar
		fields = ('rsname', 'rsregno', 'rssupervisor', 'deptname')

class ResearchScholarAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = ResearchScholarResource
	list_display = ('rsregno','rsname','deptname','rssupervisor',)
	list_filter = ('deptname',)
	
class JournalArticleResource(resources.ModelResource):
	class Meta:
		model = JournalArticle
		fields = ('refformat', 'facultyauthor', 'studentauthor', 'rsauthor', 'jtitle', 'jname', 'jstatus_choice', 'jstatus', 'jpublishedon', 'jvolno', 'jissueno', 'jpageno', 'jtr', 'jsjr', 'jsnip', 'jissn', 'pubfromconf', 'created_at','updated_at','created_by','updated_by')
		#import_id_fields=[]

class JournalArticleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = JournalArticleResource
	list_display = ('display_fauthor','display_sauthor','display_rsauthor','jtitle','jname','jstatus','jtr','jsjr','jsnip','jissn',)
	list_filter = ('jtr','jsjr','jsnip','jissn',)
	
class ConferenceArticleResource(resources.ModelResource):
	class Meta:
		model = ConferenceArticle
		fields = ('refformat','facultyauthor','studentauthor', 'rsauthor', 'ctitle','cname','presentedby', 'conferencecategory', 'cdateto', 'venue', 'country', 'csjr','csnip', 'cisbn', 'pubtojournalorbook', 'created_at', 'updated_at', 'created_by', 'updated_by')

class ConferenceArticleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = ConferenceArticleResource
	list_display = ('display_fauthor','display_sauthor','display_rsauthor','ctitle','cname','conferencecategory', 'country', 'cdatefrom','cdateto','pubtojournalorbook')
	list_filter = ('conferencecategory','country','cdatefrom','cdateto','pubtojournalorbook',)

class BookSeriesResource(resources.ModelResource):
	#facultyauthor = fields.Field(column_name='facultyauthor', widget=ManyToManyWidget(Faculty,'facultyname'))
	#studentauthor = fields.Field(column_name='studentauthor', attribute='studentauthor.set()',widget=ManyToManyWidget(Student,))
	#rsauthor = fields.Field(column_name='rsauthor', attribute='rsauthor.set()',widget=ManyToManyWidget(ResearchScholar,))
	#facultyauthor = fields.Field(column_name='facultyauthor', attribute='facultyauthor.set()', widget=ManyToManyWidget(Faculty,))
	class Meta:
		model = BookSeries
		fields = ('id','refformat', 'facultyauthor','studentauthor', 'rsauthor', 'booktitle', 'bookname', 'pubfromconf', 'bsjr', 'bsnip', 'bisbn', 'created_at', 'updated_at', 'created_by', 'updated_by')
		import_id_fields = ['id']
		
class BookSeriesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	list_display = ('display_fauthor','booktitle', 'bookname')
	resource_class = BookSeriesResource
	list_filter = ('pubfromconf','bpublishedon',)
	

class ProjectResource(resources.ModelResource):
	class Meta:
		model = Project
		fields = ('facultypi', 'facultycopi', 'student', 'rs', 'projecttitle', 'fundingagency', 'projectcategory', 'projectstatus', 'duration','sanctioneddate', 'sanctionedamount', 'fundreleasedon', 'amountreceived', 'completiondate', 'outcome', 'created_at', 'updated_at', 'created_by', 'updated_by')

class ProjectAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	resource_class = ProjectResource
	list_display = ('display_fpiauthor','display_fcopiauthor','display_sauthor', 'display_rsauthor', 'projectcategory', 'projectstatus', 'projecttitle', 'fundingagency','sanctionedamount',)
	list_filter = ('projectcategory', 'projectstatus','fundingagency','sanctioneddate',)
	fieldsets = (
        (None, {
            'fields': ('facultypi', 'facultycopi', 'student', 'rs',)
        }),
        ('Project Details', {
            'fields': ('projectcategory', 'projectstatus','projecttitle', 'fundingagency','duration','sanctioneddate','sanctionedamount','fundreleasedon','amountreceived','completiondate','outcome','created_by','updated_by',)
        }),
    )
	
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(ResearchScholar, ResearchScholarAdmin)
admin.site.register(JournalArticle, JournalArticleAdmin)
admin.site.register(ConferenceArticle, ConferenceArticleAdmin)
admin.site.register(BookSeries, BookSeriesAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Document)