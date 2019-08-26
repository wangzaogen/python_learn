## C:\Users\wangzaogen\Desktop
import os
import shutil

from static.utils import create_folder

desktop_path = 'C:/Users/wangzaogen/Desktop'
print(os.getcwd())
os.chdir(desktop_path)
print(os.getcwd())
file_type = ['.txt', '.docx', '.xmind', '.sql', '.xlsx', '.xls', '.zip', '.rar', '.py', '.xml','.pdf']
file_list = os.listdir(desktop_path)
# print(file_list)
doc = 'folder'
doc_path = create_folder(desktop_path, doc)

for ty in file_type:
    for fe in file_list:
        if (os.path.isfile(fe) and os.path.splitext(fe)[1] == ty):
            child_file_name = ty[1:]
            if(child_file_name == "xlsx" or child_file_name == "xls"):
                child_file_name = 'excle'
            if(child_file_name == "zip" or child_file_name == "rar"):
                child_file_name = 'zip'
            new_path = create_folder(doc_path,child_file_name)
            shutil.move(fe, new_path + '/' + fe)
            print(fe)


