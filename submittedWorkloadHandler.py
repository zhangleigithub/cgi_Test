#!/usr/bin/env python


import cgitb
cgitb.enable()

import cgi
import xlrd
import xlutils.copy
import datetime
import sys

form=cgi.FieldStorage()
workDate=form.getvalue('workDate','2017-03-04')
workHours=form.getvalue('workHours','7.5')
workContent=form.getvalue('workContent','Hello,world!')

rb=xlrd.open_workbook("AppData\\WorkLoad.xls","rb")
table=rb.sheets()[0]
wb=xlutils.copy.copy(rb)
s=wb.get_sheet(0)

rowindex=table.nrows;
s.write(rowindex,0,datetime.datetime.strptime(workDate,'%Y-%m-%d'))
s.write(rowindex,1,workHours)
s.write(rowindex,2,workContent.decode('UTF-8'))
wb.save("AppData\\WorkLoad.xls")

print("content-type:text/html")
print("")
print("successful")