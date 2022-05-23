from logging.config import valid_ident
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Admin, Staff,Student, User,question_paper
import random
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


def admin_home(request):
    
    return render(request, 'Admin/admin_home.html')

def admin_staff_view(request):
    staffs=Staff.objects.all() 
    staff_name_list=[]
    for staff in staffs:
        staff_name_list.append(staff.admin.username)
   
    return render(request, 'Admin/admin_staff_view.html',{ 'staff_list':staffs})

def admin_student_view(request):
    students=Student.objects.all()
    student_name_list=[]

    for student in students:
        student_name_list.append(student.admin.username)
    return render(request, 'Admin/admin_student_view.html', {'student_list':students})

def delete(request, id):
    staff = User.objects.get(id=id)
    staff.delete()
    return redirect('admin_staff_view')

def AdminLoginPage(request):
    return render(request,"Admin/admin_login_page.html")



def random_question(request):
    test = question_paper.objects.all()
    paper_list = []
    for i in test:
        i= i.paper
        paper_list.append(i)
    print(paper_list)

    mode = random.choice(paper_list)
    # print(mode)
    return mode 

