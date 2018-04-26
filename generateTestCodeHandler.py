#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgi, os
import cgitb; cgitb.enable()
import GenerateTestCode

try:
   import msvcrt  
   msvcrt.setmode(0, os.O_BINARY) # stdin  = 0  
   msvcrt.setmode(1, os.O_BINARY) # stdout = 1  
except ImportError:  
    pass

# 表单数据
form = cgi.FieldStorage()

# 获取文件名
fileitem = form['fileName']

# Generator to buffer file chunks  
def fbuffer(f, chunk_size=10000):  
   while True:  
      chunk = f.read(chunk_size)  
      if not chunk: break  
      yield chunk

# 检测文件是否上传
if fileitem.filename:
   # 设置文件路径 
   fn = os.path.basename(fileitem.filename)
   fileName='upload\\' + fn;
   fo=open(fileName, 'wb');
   for chunk in fbuffer(fileitem.file):
      fo.write(chunk);
   fo.close();

   files=GenerateTestCode.GenerateTestCode(fileName,"output\\");
   req=[];
   for item in files:
      req.append('<a href="viewTestCodeHandler.py?fileName='+item+'" target="_blank">'+os.path.basename(item)+'</a>'+'<a href="'+item+u'">下载</a>');
else:
   message = '文件没有上传'

print "Content-Type: text/html\n"
print "<html>"
print "<head>"
print '<meta charset="utf-8">'
print "<title>GenerateResult</title>"
print '<link rel="icon" href="./images/favicon.png" />'
print '<link rel="stylesheet" type="text/css" href="./css/bootstrap.min.css">'
print "</head>"
print "<body>"
print '<div class="panel panel-default">'
print '<div class="panel-body">'
print "<p>测试代码：</p>"
print "\n".join(req).encode('utf-8');
print '<div class="panel-footer">TestCode.</div>'
print '</div>'
print '</div>'
print "</body>"
print "</html>"
