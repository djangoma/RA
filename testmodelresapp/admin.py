from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Faculty,Department, Student, ResearchScholar, JournalArticle, ConferenceArticle, BookSeries, Project
# Register your models here.
from import_export import resources
from import_export.admin import ImportExportActionModelAdmin
#from core.models import 


class DepartmentResource(resources.ModelResource):
	class Meta:
		model = Department
		fields = ('deptname')

class DepartmentAdmin(ImportExportModelAdmin):
	resource_class = DepartmentResource

	
class FacultyResource(resources.ModelResource):
    class Meta:
        model = Faculty
        fields = ('empid','facultyname', 'deptname')
        export_order = ('empid','facultyname', 'deptname')
		
class FacultyAdmin(ImportExportModelAdmin):
	resource_class = FacultyResource
	
class StudentResource(resources.ModelResource):
	class Meta:
		model = Student
		fields = ('sregno', 'sname', 'sbranch', 'deptname', 'sbatch', 'studentcategory')
		
class StudentAdmin(ImportExportModelAdmin):
	resource_class = StudentResource
#class DepartmentAdmin(ImportExportActionModelAdmin):
#	pass
	
class ResearchScholarResource(resources.ModelResource):
	class Meta:
		model = ResearchScholar
		fields = ('rsname', 'rsregno', 'rssupervisor', 'deptname')

class ResearchScholarAdmin(ImportExportModelAdmin):
	resource_class = ResearchScholarResource
	
class JournalArticleResource(resources.ModelResource):
	class Meta:
		model = JournalArticle
		fields = ('refformat', 'facultyauthor', 'studentauthor', 'rsauthor', 'jtitle', 'jname', 'jstatus_choice', 'jstatus', 'jpublishedon', 'jvolno', 'jissueno', 'jpageno', 'jtr', 'jsjr', 'jsnip', 'jissn', 'pubfromconf', 'created_at','updated_at','created_by','updated_by')

class JournalArticleAdmin(ImportExportModelAdmin):
	resource_class = JournalArticleResource
	
class ConferenceArticleResource(resources.ModelResource):
	class Meta:
		model = ConferenceArticle
		fields = ('refformat','facultyauthor','studentauthor', 'rsauthor', 'ctitle','cname','presentedby', 'conferencecategory', 'cdateto', 'venue', 'country', 'csjr','csnip', 'cisbn', 'pubtojournalorbook', 'created_at', 'updated_at', 'created_by', 'updated_by')

class ConferenceArticleAdmin(ImportExportModelAdmin):
	resource_class = ConferenceArticleResource

class BookSeriesResource(resources.ModelResource):
	class Meta:
		model = BookSeries
		fields = ('id','refformat', 'facultyauthor','studentauthor', 'rsauthor', 'booktitle', 'bookname', 'pubfromconf', 'bsjr', 'bsnip', 'bisbn', 'created_at', 'updated_at', 'created_by', 'updated_by')
		import_id_fields = ['id']
		
class BookSeriesAdmin(ImportExportModelAdmin):
	resource_class = BookSeriesResource

class ProjectResource(resources.ModelResource):
	class Meta:
		model = Project
		fields = ('facultypi', 'facultycopi', 'student', 'rs', 'projecttitle', 'fundingagency', 'projectcategory', 'projectstatus', 'duration','sanctioneddate', 'sanctionedamount', 'fundreleasedon', 'amountreceived', 'completiondate', 'outcome', 'created_at', 'updated_at', 'created_by', 'updated_by')

class ProjectAdmin(ImportExportModelAdmin):
	resource_class = ProjectResource
	
admin.site.register(Department, DepartmentAdmin)
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(ResearchScholar, ResearchScholarAdmin)
admin.site.register(JournalArticle, JournalArticleAdmin)
admin.site.register(ConferenceArticle, ConferenceArticleAdmin)
admin.site.register(BookSeries, BookSeriesAdmin)
admin.site.register(Project, ProjectAdmin)