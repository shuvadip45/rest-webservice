from django.shortcuts import render
import pandas as pd
from django.http import HttpResponse

df=pd.read_csv('media/bank_branches.csv')


def home(request):
    return render(request, 'home.html')

def bankdetails(request,ifsc):
    df1=df.loc[df['ifsc']==ifsc]
    return HttpResponse(df1.to_html())



def bankbranches(request, bankname, city):
    df1=df.loc[(df['bank_name']==bankname) & (df['city']==city)]
    return HttpResponse(df1.to_html())
