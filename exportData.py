import subprocess
import chardet
import sys

table_name = input("请输入表名：\n")
print("文件路径例子:{},\n".format("D://downloads//number.csv"))
file_path = input("请输入CSA文件绝对路径（文件名只能包含文件和数字）：\n")

command = "java -jar admin-service.jar"

arg0 = table_name
arg1 = file_path
cmd = [command, arg0, arg1]
new_cmd = " ".join(cmd)
stdout, stderr = subprocess.Popen(
    new_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
# encoding = chardet.detect(stdout)["encoding"]
# result = stdout.decode(encoding)
# print(result)
