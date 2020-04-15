import tkinter
import tkinter.messagebox
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename
import subprocess

top = tkinter.Tk()
top.title('导数据')
top.geometry('500x400+850+360')

path = tkinter.StringVar()
tkinter.Label(top,text = "导入的表名:").grid(row = 0, column = 0)
table = tkinter.Entry(top, show = None)
table.grid(row = 0, column = 1)

tkinter.Label(top,text = "CSV目标路径:").grid(row = 1, column = 0)
file_path_name = tkinter.Entry(top, textvariable = path)
file_path_name.grid(row = 1, column = 1)


def selectPath():
    path_ = askopenfilename()
    path_array = str(path_).split('/')
    window_path = '//'.join(path_array)
    path.set(window_path)
    print(window_path)

def export():
    table_name = table.get()
    file_path = file_path_name.get()
    command = "java -jar admin-service.jar"


    if table_name == '' or file_path== '':
        tkinter.messagebox.showerror(title='Hi',message='表名和路径不能为空')


    cmd = [command,table_name,file_path]
    new_cmd = " ".join(cmd)
    subprocess.Popen(new_cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()

tkinter.Button(top, text = "选择需要导入的CSV文件", command = selectPath).grid(row = 1, column = 2)

tkinter.Button(top, text = "开始导入", command = export).grid(row = 3, column = 2)

top.mainloop()