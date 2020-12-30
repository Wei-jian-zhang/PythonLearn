'''
简易的命令行文件管理系统。
功能：
1.用户输入指定路径，显示路径下所有文件和文件夹。
2.主界面展示当前所有文件和文件夹，显示文件和文件夹的名称和属性，是文件或者文件夹。
  filename  文件
  dirname   文件夹
3.使用cd filepath的形式进入指定的文件夹，如果不是文件夹，给于提示。
4.使用cd .. 返回上一层目录。
5.使用cd .展示当前目录路径。
6.使用mkfile filename的形式在当前目录创建文件。
7.使用mkdir dirname的形式在当前目录创建文件夹。
8.使用cp sorcefile targetfile的形式支持复制文件和文件夹。
9.使用re filename的形式提供文件或者文件夹的重命名。
9.使用del filename的形式提供文件或者文件夹删除，要提供确实删除的信息。

ps：使用python的os库完成。
'''

# -*- coding: utf-8 -*-
# coding=utf-8
import os


def Main(path, dept):
    """
    主函数
    """
    PrintFoldList(path)
    GetUserControl(path, dept)


def copy(src_path, target_path):
    """
    复制文件或文件夹
    """
    if os.path.isdir(src_path):  #如果src_path是目录
        filelist1 = os.listdir(src_path)  #返回这个文件夹的名字的列表
        for file in filelist1:
            path = os.path.join(src_path, file) #遍历列表，把目录和文件名合成一个路径
            if os.path.isdir(path): #如果path是目录
                path1 = os.path.join(target_path, file) #target_path和file合成一个路径东北关于path1
                os.mkdir(path1)  #创建一个名为path1的文件夹
                copy(path, path1) #复制这两个
            else:
                with open(path, "rb") as f1: #以二进制形式打开，写入f1读取
                    container = f1.read()
                    path2 = os.path.join(target_path, file)
                    with open(path2, "wb") as f2:
                        f2.write(container)  #二进制形式打开写入
    else:
        print("复制完成")


def Delfile(path, name):
    """
    删除文件或者文件夹
    """
    fpath = path + '/' + name
    if os.path.exists(fpath):  #判断路径存在完好
        if os.path.isfile(fpath):  #判断路径是否为文件
            os.remove(fpath)  #如果为文件，删除
        if os.path.isdir(fpath):
            os.removedirs(fpath)  #如果fpath为目录,递归删除


def Rename_file(path, newname):
    """
    重命名文件或者文件夹
    """
    if os.path.exists(path):
        if os.path.isdir(path):
            f = os.path.dirname(path)  #f为返回文件路径
            newfold_name = os.path.join(f, newname)
            os.rename(path, newfold_name)  #更新为新的名字
        if os.path.isfile(path):  #如果是文件
            dirname = os.path.dirname(path)  #返回文件路径
            New_name = os.path.join(dirname, newname)  #合成为一个路径
            os.rename(path, New_name)  #改为新的文件名


def mkdir(path, foldername):
    """
    新建一个新的文件夹，若文件夹存在则不创建
    """
    if os.path.exists(path):
        if os.path.exists(path + '/' + foldername):  #如果文件已存在
            print("文件夹已经存在,无法创建!")
        else:
            folderpath = path + '/' + foldername  #合成folderpath文件夹的路径
            os.mkdir(folderpath)  #创建文件夹
            if os.path.exists(folderpath):  #检查是否存在
                print("文件夹", foldername, "创建成功!")
            else:
                print("文件夹", foldername, "创建成功!")


def mkfile(path, filename, msg=None):
    """
    新建一个新的文件，若文件存在则不创建
    """
    if os.path.exists(path):  #判断路径
        if os.path.exists(path + '/' + filename):  #判断文件
            print("文件已经存在,无法创建!")
        else:
            filepath = path + '/' + filename
            if msg:
                f = open(filepath, 'w')
                f.write(msg)
                f.close()
                if os.path.exists(filepath):
                    print("文件", filename, "创建成功!")
                else:
                    print("文件", filename, "创建失败!")
            else:
                f = open(filepath, 'w')
                f.close()
                if os.path.exists(filepath):  #如果文件存在
                    print("文件", filename, "创建成功!")
                else:
                    print("文件", filename, "创建失败!")


def PrintFoldList(path):
    """
    输出
    """
    i=os.system("cls")
    pathlist = os.listdir(path)  #返回path文件的内容
    print("当前路径为：", path)
    print("--------------------------------")
    print('名称'.ljust(20), " 类型")
    print("--------------------------------")
    for f in pathlist:
        if os.path.isfile(path + '/' + f):  #判断此路径是否是文件
            if len(f) < len(f.encode('GBK')):
                print(f.ljust(20 - (len(f.encode('GBK')) - len(f))), "  文件")
            else:
                print(f.ljust(20), "  文件")
        else:
            if len(f) < len(f.encode('GBK')):
                print(f.ljust(20 - (len(f.encode('GBK')) - len(f))), "  文件夹")
            else:
                print(f.ljust(20), "  文件夹")

    print("--------------------------------")


def GetUserControl(path, dept):
    """
    获取用户当前操作
    """
    control = input()

    clist = control.split(' ')
    if clist is not None:  #如果用户输入的不是空
        if clist[0].lower() == 'cd':  #将列表输入的第一个字母改为小写
            if clist[1] is not None:  #如果列表的第二个元素不是空
                if clist[1] == "..":  #如果第二个元素是..
                    if dept == 0:
                        print("当前已经是根目录！")
                        input("按enter继续")
                        Main(path, dept)
                    else:
                        Newpath = os.path.abspath(os.path.join(path, ".."))  #3返回路径的绝对路径
                        dept = dept - 1  #返回上一层
                        Main(Newpath, dept)  #重新打开
                elif clist[1] == ".":  #列表的第二个元素是.
                    print("当前路径为：", path)
                    input("按enter继续")
                    Main(path, dept)
                else:
                    Newpath = path + '/' + clist[1]
                    if os.path.isdir(Newpath):
                        if os.path.exists(Newpath):
                            dept = dept + 1
                            Main(Newpath, dept)
                        else:
                            print("你输入了错误的的路径名称，请重新输入。")
                            GetUserControl(path, dept)
                    else:
                        print(clist[1], "不是一个文件夹")
                        GetUserControl(path, dept)
            else:
                print("你请输入正确的路径或者操作符.")
                input("按enter继续")
                Main(path, dept)
        elif clist[0].lower() == 're':  #输入的第一个元素是re
            if clist[1] is not None:
                cPath = path + '/' + clist[1]  #整合文件路径
                if os.path.exists(cPath):  #判断文件路径是否存在
                    newname = input("请输入新文件或文件夹的名称:")
                    print("将重命名:", clist[1])
                    print("新名称:", newname)
                    Rename_file(cPath, newname)  # 调用更名寒暑表
                    input("按enter继续")
                    Main(path, dept)   #重新调用函数
                else:
                    print("你输入的名称不存在当前路径!")
                    GetUserControl(path, dept)
            else:
                print("文件名称不能为空!")
                GetUserControl(path, dept)
        elif clist[0].lower() == 'mkfile':
            if clist[1] is not None:
                print("将在当前目录尝试创建名称为: ", clist[1], "的文件...")
                mkfile(path, clist[1])
                input("按enter继续")
                Main(path, dept)
            else:
                print("文件名称不能为空!")
                GetUserControl(path, dept)
        elif clist[0].lower() == 'mkdir':
            if clist[1] is not None:
                print("将在当前目录尝试创建名称为: ", clist[1], "的文件夹...")
                mkdir(path, clist[1])
                input("按enter继续")
                Main(path, dept)
            else:
                print("文件名称不能为空!")
                GetUserControl(path, dept)
        elif clist[0].lower() == 'del':
            if clist[1] is not None:
                tpath = path + '/' + clist[1]
                if os.path.exists(tpath):
                    if os.path.isfile(tpath):
                        print("将要删除文件", clist[1], "是否确认? y/n")
                        result = input()
                        if result.lower() == "y":
                            Delfile(path, clist[1])
                            input("按enter继续")
                            Main(path, dept)
                        elif result.lower() == "n":
                            GetUserControl(path, dept)
                        else:
                            print("你输入了错误的操作符!")
                            input("按enter继续")
                            Main(path, dept)
                    if os.path.isdir(tpath):
                        print("将要删除文件夹", clist[1], "是否确认? y/n")
                        result = input()
                        if result.lower() == "y":
                            Delfile(path, clist[1])
                            input("按enter继续")
                            Main(path, dept)
                        elif result.lower() == "n":
                            GetUserControl(path, dept)
                        else:
                            print("你输入了错误的操作符!")
                            input("按enter继续")
                            Main(path, dept)
            else:
                print("文件名称不能为空!")
                GetUserControl(path, dept)
        elif clist[0].lower() == 'cp':
            if clist[1] is not None:
                if clist[2] is not None:
                    srcpath = path + '/' + clist[1]
                    if os.path.exists(srcpath):
                        if os.path.isdir(srcpath):
                            print("复制文件夹:", clist[1])
                            copy(srcpath, clist[2])
                            input("按enter继续")
                            Main(path, dept)
                        else:
                            print("复制文件:", clist[1])
                            copy(srcpath, clist[2])
                            input("按enter继续")
                            Main(path, dept)
                    else:
                        print("你输入的路径不存在!")
                        GetUserControl(path, dept)
                else:
                    print("路径不能为空!")
                    GetUserControl(path, dept)
            else:
                print("路径不能为空!")
                GetUserControl(path, dept)
        elif clist[0].lower() == 'quit':
            pass
        else:
            print("请输入有效的操作符!")
            GetUserControl(path, dept)
    else:
        GetUserControl(path, dept)


def Start():
    """
    docstring
    """
    path = input("请输入文件夹路径：")
    if os.path.exists(path):   #如果文件夹存在
        return path   #返回路径
    else:
        print("你输入的路径不存在，请重新输入！")  #如果路径不存在，重新执行函数
        input("按enter继续")
        Start()


if __name__ == "__main__":
    path = Start()
    dept = 0
    Main(path, dept)
    print("系统已经退出.....")