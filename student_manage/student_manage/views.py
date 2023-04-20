
import pymysql
from django.shortcuts import render

fn = ""
st = " "
ln = ""
g = ""
rn = ""
dob = ""


def BASE(request):
    return render(request, 'base.html')


def STUDENTDETAILS(request):
    return render(request, 'studentdetails.html')


def ADD(request):
    return render(request, 'add.html')


def adddata(request):
    global fn, st, ln, g, rn, dob, cl
    if request.method == "GET":
        m = pymysql.connect(host="localhost", user="root", password="saurav123", database="student_management")
        cursor = m.cursor()
        d = request.GET
        for key, value in d.items():
            if key == "fname":
                fn = value
            if key == "lname":
                ln = value
            if key == "st_id":
                st = int(value)
            if key == "gender":
                g = value
            if key == "roll_no":
                rn = int(value)
            if key == "dob":
                dob = value
            if key == "class":
                cl = int(value)
        c = "insert into student(st_id, first_name,last_name,gender,roll_no,dob,class_id) values('{}','{}','{}','{}'," \
            "'{}','{}','{}')".format(st, fn, ln, g, rn, dob, cl)
        cursor.execute(c)
        m.commit()
        return render(request, 'base.html')
    else:
        return render(request, 'marks.html')


def REMOVE(request):
    return render(request, 'remove.html')


def MARKS(request):
    return render(request, 'marks.html')
