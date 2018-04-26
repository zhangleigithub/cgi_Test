#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import xlrd
import codecs

# 测试代码生成
def GenerateTestCode(useCaseFile,outputPath):
    files=[];
    name="${Name}";
    className="${ClassName}";
    useCaseNumber="${UseCaseNumber}";
    groupType="${GroupType}";
    methodName="${MethodName}";

    nameValue="";
    classNameValue="";
    useCaseNumberValue="";
    groupTypeValue="";
    methodNameValue="";

    templateHeader='';
    templateClass='';
    templateMethod='';

    isHeader=True;
    isClass=False;
    isMethod=False;

    # 打开模板
    templateFile=codecs.open("Template.java","r",encoding='utf-8');

    # 读取模板
    for line in templateFile:
        if line.strip()=="//region Class":
            isHeader=False;
            isClass=True;
            isMethod=False;
            continue;
        if line.strip()=="//region Method":
            isHeader=False;
            isClass=False;
            isMethod=True;
            templateClass+="${Mehtod}\n";
            continue;
        if line.strip()=="//endregion" and isMethod:
            isHeader=False;
            isClass=True;
            isMethod=False;
            continue;
        if line.strip()=="//endregion" and isClass:
            isHeader=False;
            isClass=False;
            isMethod=False;
            break;
        if isHeader:
            templateHeader+=line;
        elif isClass:
            templateClass+=line;
        elif isMethod:
            templateMethod+=line;

    # 关闭模板
    templateFile.close();

    # 用例集
    listUseCase=[];

    # 打开excel
    workbook=xlrd.open_workbook(useCaseFile,'rb');

    # 读取Excel
    for sheet in workbook.sheets():
        # 文件头
        row_data = sheet.row_values(3);
        nameValue=row_data[13].encode('utf-8').decode('utf-8');

        # 用例集
        row_data=sheet.row_values(4);
        for j in range(26,len(row_data)):
            useCaseNumberValue=row_data[j].encode("utf-8").decode('utf-8');
            
            if useCaseNumberValue=="":
                continue;
            
            strType=sheet.row_values(sheet.nrows-1)[j].encode("utf-8").decode('utf-8');
            
            if strType==u'正':
                groupTypeValue='normal';
            elif strType==u'异':
                groupTypeValue='abnormal';
            elif strType==u'边':
                groupTypeValue='boundary';
            else:
                groupTypeValue="None";
	    
            methodNameValue=useCaseNumberValue.lower().replace("scl", "st").replace("-", "_");
            
            # 添加到集合
            listUseCase.append(templateMethod.replace(useCaseNumber, useCaseNumberValue).replace(groupType, groupTypeValue).replace(methodName, methodNameValue));

	# 写入文件
        classNameValue=sheet.name.lower().replace("scl", "st").replace("-", "_").encode("utf-8").decode('utf-8');
        fileName=outputPath+classNameValue+".java";
        files.append(fileName);
        fo=codecs.open(fileName,"w+",encoding='utf-8');
        fo.write(templateHeader);
        fo.write(templateClass.replace(name, nameValue).replace(className, classNameValue).replace("${Mehtod}", "\n".join(listUseCase).rstrip()));
        fo.close();

    return files;

if __name__ == '__main__':
    if len(sys.argv)==1 or sys.argv[1]=="" or sys.argv[2]=="":
        print "argv[1]:源文件路径";
        print "argv[2]:目的文件路径";
    else:
        #调用测试代码生成
        files=GenerateTestCode(sys.argv[1],sys.argv[2]);
        for fileName in files:
            print fileName;
        print "Completed"
             
            
