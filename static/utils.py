import os


##path 路径下 name 文件夹是否存在，不存在则创建
##return 创建的文件夹路径
def create_folder(path, name):
    new_path = path +'/'+ name;
    if (os.path.exists(new_path)):
        # print(new_path+",this folder is exists")
        pass
    else:
        os.mkdir(new_path)

    return new_path



def checkFinished(browser):
    flag = 1
    context =  browser.find_element_by_class_name("console-output").text
    lastStr = str(context)[-10:]
    if int(lastStr.find('Finished: SUCCESS')) < 0 :
        browser.refresh()
        checkFinished(browser)
    else:
        return flag