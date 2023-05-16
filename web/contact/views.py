from django.shortcuts import render
import mysql.connector as sql

fn = ''
ln = ''
em = ''
pwd = ''



# Create your views here.
def contactINF(request):
    global fn, ln, em, pwd
    if request.method == "POST":
        m = sql.connect(host="localhost", user="root", passwd="Mangesh@1011", database='yahoo',
                        auth_plugin='mysql_native_password')
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "first_name":
                fn = value
            if key == "last_name":
                ln = value
            if key == "email":
                em = value
            if key == "contact_no":
                pwd = value

        c = "insert into contactINF Values('{}','{}','{}','{}')".format(fn, ln, em, pwd)
        cursor.execute(c)
        m.commit()

    return render(request, 'contact_page.html')