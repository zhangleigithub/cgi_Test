#!/usr/bin/env python

import cgitb
cgitb.enable()

import cgi
import xlrd
import json

form=cgi.FieldStorage()
rows=int(form.getvalue('rows',10))
page=int(form.getvalue('page',1))

startIndex=rows * (page - 1)
endIndex=rows * page;

rb=xlrd.open_workbook("AppData\\WorkLoad.xls","rb")

table=rb.sheets()[0]

lst=[]

print("Content-type:application/json")
print("")

for i in range(table.nrows):
    if i>=startIndex and i<endIndex:
        info={}
        info["ID"]=i+1;
        info["workData"]=xlrd.xldate.xldate_as_datetime(table.row_values(i)[0],1).strftime('%Y-%m-%d');
        info["workHours"]=table.row_values(i)[1];
        info["workContent"]=table.row_values(i)[2];
        lst.append(info)

info={}
info["total"]=table.nrows;
info["rows"]=lst;

print(json.dumps(info))