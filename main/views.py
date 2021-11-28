from django.shortcuts import render
from django.http import HttpResponse
import openpyxl
import os
from course.models import Courses
from category.models import Category

# Create your views here.
def home_view(request):
    return render(request, 'main/home.html')

def import_excel(request):
    path = os.path.join(os.path.expanduser('~'), 'Downloads', 'Undergraduate CSE Electives.xlsx')
    wb = openpyxl.load_workbook(filename=path, data_only=True)['Sheet1']
    rows = []
    for i in range(1, wb.max_row+1):
        row = [cell.value for cell in wb[i][0:7+1]] # sheet[n] gives nth row (list of cells)
        rows.append(row)
    for index,row in enumerate(rows):
        if index > 0:
            course = Courses.objects.get(name=row[0])
            # course_categories = row[6].split(",")
            # course_categories = [x.strip() for x in course_categories]
            # for category in course_categories:
            #     category = Category.objects.get(name=category)
            #     course.categories.add(category)
    return HttpResponse(200)