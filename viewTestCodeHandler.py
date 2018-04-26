#!/usr/bin/python
# -*- coding: UTF-8 -*-

import cgi, os
import cgitb; cgitb.enable()
import GenerateTestCode
import codecs

try:
   import msvcrt  
   msvcrt.setmode(0, os.O_BINARY) # stdin  = 0  
   msvcrt.setmode(1, os.O_BINARY) # stdout = 1  
except ImportError:  
    pass

# 表单数据
form = cgi.FieldStorage()

# 获取文件名
fileName = form.getvalue('fileName')

print "Content-Type: text/html\n"
print "<html>"
print "<head>"
print '<meta charset="utf-8">'
print "<title>"+os.path.basename(fileName)+"</title>"
print '<script type="text/javascript" src="js/syntaxhighlighter_3.0.83/scripts/shCore.js"></script>'
print '<script type="text/javascript" src="js/syntaxhighlighter_3.0.83/scripts/shBrushJava.js"></script>'
print '<link type="text/css" rel="stylesheet" href="js/syntaxhighlighter_3.0.83/styles/shCoreEclipse.css"/>'
print '<link type="text/css" rel="stylesheet" href="js/syntaxhighlighter_3.0.83/styles/shThemeEclipse.css"/>'
print "</head>"
print "<body>"
print '<pre class="brush: java">'

lines=[];
fo=codecs.open(fileName, 'r',encoding='utf-8');
for line in fo:
   lines.append(line.encode('utf-8'));
fo.close();
print ''.join(lines);

print "</pre>"
print '<script type="text/javascript">'
print 'SyntaxHighlighter.all()'
print '</script>'
print "</body>"
print "</html>"
