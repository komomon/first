import os
#调用时格式为， py文件名.函数名()
def input_content1(file_name,file_type,write_content):      ##保存文本数据
    fileName=file_name+'.'+file_type
    f = open(fileName, 'w',encoding='utf-8')
    f.write(write_content)
    print("——————写入完成。——————")
    f.close()
def input_content2(file_name,file_type,write_content):      #保存二进制数据
    fileName=file_name+'.'+file_type
    f = open(fileName, 'wb')
    f.write(write_content)
    print("——————写入完成。——————")
    f.close()
#调用格式为，路径，文件名 比如：creat_folder(r'C:\Users\98483\Desktop','11111')
def creat_folder(path,folder_name):
    #调用时记得路径path前加个 r
    path=path+'\\'+folder_name
    if not os.path.exists(path):  #如果文件夹不存在则创建它
        os.mkdir(path)
    return path
