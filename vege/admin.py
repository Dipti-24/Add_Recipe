from django.contrib import admin

# Register your models here.
from .models import*
admin.site.register(Recipe)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)



class SubjectMarkAdmin(admin.ModelAdmin):
    list_display=['student','subject',"marks"]

admin.site.register(SubjectMarks,SubjectMarkAdmin)



from django.db.models import Sum

class ReportCardAdmin(admin.ModelAdmin):
    list_display=['student','student_rank','total_marks','date_of_report_card_generation']
    
    ordering=['student_rank']

    def total_marks(self,obj):
        subject_marks=SubjectMarks.objects.filter(student=obj.student)
        #ordering=['student_rank']
        marks=(subject_marks.aggregate(marks=Sum('marks')))
        print(marks['marks'])
        return 0
    


admin.site.register(ReportCard,ReportCardAdmin)

