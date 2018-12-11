from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse
from django.db import connection
import json

cursor=connection.cursor()

def home(request):
    return render(request, 'home.html')

def bankdetails(request,ifsc):
    cursor.execute("SELECT * FROM mytable WHERE ifsc=(%s)", [ifsc])
    rows=cursor.fetchall()
    print(rows)
    return HttpResponse(json.dumps(rows),content_type="application/json")



def bankbranches(request, bankname, city):
    cursor.execute("SELECT * FROM mytable WHERE bank_name=(%s) AND city=(%s)", [bankname,city])
    rows=cursor.fetchall()
    return HttpResponse(json.dumps(rows),content_type="application/json")
