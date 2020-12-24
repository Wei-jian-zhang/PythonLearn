# -*- coding: utf-8 -*-
import codecs
import json
import random
import time
import tkinter.messagebox as messagebox
from tkinter import *

import requests


class ProBar(object):
    """
    用于显示进度条！
    """
    _ProgressBar: Tk

    def __init__(self, count):
        self.count = count
        self._ProgressBar = Tk()
        self._ProgressBar.title('正在获取评论区所有的用户，请稍候....')
        # 设置窗口居中
        # max_w:屏幕最大宽度,max_h:屏幕最大高度
        max_w, max_h = self._ProgressBar.maxsize()
        # 窗口的宽度和高度
        wiw = 800
        wih = 200
        # 计算中心坐标
        cen_x = (max_w / 2) - (wiw / 2)
        cen_y = (max_h / 2) - (wih / 2)
        # 设置窗口大小和位置
        self._ProgressBar.geometry('%dx%d+%d+%d' % (wiw, wih, cen_x, cen_y))
        self._ProgressBar.resizable(False, False)
        self._ProgressBar.config(bg='#535353')
        self.canvas_progress_bar = Canvas(self._ProgressBar, width=630, height=20)
        self.canvas_shape = self.canvas_progress_bar.create_rectangle(0, 0, 0, 25, fill='green')
        self.canvas_text = self.canvas_progress_bar.create_text(292, 4, anchor=NW)
        self.canvas_progress_bar.itemconfig(self.canvas_text, text='00:00:00')
        self.var_progress_bar_percent = StringVar()
        self.var_progress_bar_percent.set('00.00  %')
        self.label_progress_bar_percent = Label(self._ProgressBar, textvariable=self.var_progress_bar_percent,
                                                fg='#F5F5F5', bg='#535353')
        self.canvas_progress_bar.place(relx=0.45, rely=0.4, anchor=CENTER)
        self.label_progress_bar_percent.place(relx=0.89, rely=0.4, anchor=CENTER)

        # self._ProgressBar.mainloop()

    def update_progress_bar(self, steps):
        percent = int((steps / self.count) * 100)
        hour = int(steps / 3600)
        minute = int(steps / 60) - hour * 60
        second = steps % 60
        green_length = int(630 * percent / 100)

        self.canvas_progress_bar.coords(self.canvas_shape, (0, 0, green_length, 25))
        self.canvas_progress_bar.itemconfig(self.canvas_text, text='%02d:%02d:%02d' % (hour, minute, second))
        self.var_progress_bar_percent.set('%0.2f  %%' % percent)
        if steps == self.count:
            self._ProgressBar.destroy()
            MainPage()
        else:
            self._ProgressBar.update()


class StartPage(object):
    """
    登陆页面
    """

    def bf_goMainPage(self):
        """
        跳转函数
        """
        print(self.test.get())
        abid = self.test.get()

        if len(abid) == 0:
            messagebox.showinfo('提示', '请输入有效的AV/BV号！')
        else:
            aid = abid[0:2]

            if aid.lower() == "av":
                if av2bv(abid) == 0:
                    messagebox.showinfo('提示', '无效的AV／BV号!')
                else:
                    self.root.destroy()
                    getAllcoment(abid)
            elif aid.lower() == "bv":
                if bv2av(abid) == 0:
                    messagebox.showinfo('提示', '无效的AV／BV号!')
                else:
                    self.root.destroy()
                    av_id = bv2av(abid)
                    getAllcoment(av_id)
            else:
                messagebox.showinfo('提示', '无效的AV／BV号!')

    def __init__(self):
        self.root = Tk()
        # 设置窗口居中
        # max_w:屏幕最大宽度,max_h:屏幕最大高度
        max_w, max_h = self.root.maxsize()
        # 窗口的宽度和高度
        wiw = 600
        wih = 200
        # 计算中心坐标
        cen_x = (max_w / 2) - (wiw / 2)
        cen_y = (max_h / 2) - (wih / 2)
        self.root.geometry('%dx%d+%d+%d' % (wiw, wih, cen_x, cen_y))
        self.root.resizable(False, False)
        self.test = StringVar()
        Label(self.root, text="请输入AV/BV号：").place(relx=0.3, rely=0.5, anchor=CENTER)
        Entry(self.root, textvariable=self.test).place(relx=0.5, rely=0.5, anchor=CENTER)
        Button(self.root, text="搜索", command=self.bf_goMainPage).place(relx=0.7, rely=0.5, anchor=CENTER)

        self.root.mainloop()


class MainPage(object):
    """
    注册页面
    """

    def bf_goLogin(self):
        """
        跳转函数
        """
        self.root.destroy()

    def __init__(self):
        self.root = Tk()
        # 设置窗口居中
        # max_w:屏幕最大宽度,max_h:屏幕最大高度
        max_w, max_h = self.root.maxsize()
        # 窗口的宽度和高度
        wiw = 800
        wih = 400
        # 计算中心坐标
        cen_x = (max_w / 2) - (wiw / 2)
        cen_y = (max_h / 2) - (wih / 2)
        self.root.geometry('%dx%d+%d+%d' % (wiw, wih, cen_x, cen_y))
        self.root.resizable(False, False)

        iframe = Frame(self.root)

        lb = Listbox(iframe, height=200, width=600)
        scr = Scrollbar(iframe)

        lb.config(yscrollcommand=scr.set)
        scr.config(command=lb.yview)
        with open("Data\\data.json") as file_obj:
            users = json.load(file_obj)

        userlist = users["user"]
        usernumber = len(userlist)

        for i in range(0, usernumber - 1):
            lb.insert(END, userlist[i])

        lb.pack(side=LEFT, fill=Y)
        scr.pack(side=RIGHT, fill=Y)

        iframe.place(relx=0.0, rely=0.222, relheight=0.789, relwidth=0.999)

        self.Button1 = Button(self.root)
        self.Button1.place(relx=0.281, rely=0.133, height=28, width=49)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text="Button1")

        self.Entry1 = Entry(self.root)
        self.Entry1.place(relx=0.163, rely=0.133, height=27, relwidth=0.109)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Label1 = Label(self.root)
        self.Label1.place(relx=0.015, rely=0.133, height=23, width=97)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text="Label")

        self.root.mainloop()


def av2bv(avid):
    site = "https://api.bilibili.com/x/web-interface/view?aid=" + str(avid)
    lst = codecs.decode(requests.get(site).content, "utf-8").split("\"")
    if int(lst[2][1:-1]) != 0:
        return 0
    return lst[13]


def bv2av(bvid):
    site = "https://api.bilibili.com/x/web-interface/view?bvid=" + bvid
    lst = codecs.decode(requests.get(site).content, "utf-8").split("\"")
    if int(lst[2][1:-1]) != 0:
        return 0
    return int(lst[16][1:-1])


def getAllcoment(av_id):
    r = requests.get('https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=1&oid={}&sort=2'.format(av_id))
    # 这个json地址获取方法：随便找一个评论用户的ID，在网页F12中CTRL+f 搜索 ，可以找到一个地址，复制地址，去掉callback回调部分
    data = json.loads(r.text)
    page_count = (data['data']['page']['count']) // 20 + 1  # 获取总页数，本来想用xpath直接爬到总页数，后来发现json里有个count总楼层数统计，所以可以计算出总页数
    # pprint.pprint(data['data']['replies'])
    # 这个json里不只有用户id ，而且能找到用户评论，楼中楼的用户ID 评论等
    user_list = []  # 保存用户名
    pb = ProBar(page_count)

    for pg_num in range(1, page_count + 1):  # 循环获取所有页面上的用户名，这地方运行速度慢，后续尝试利用多线程加快速度
        time.sleep(1)
        print('爬取第{}页...'.format(pg_num))
        r = requests.get(
            'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn={}&type=1&oid={}&sort=2'.format(pg_num, av_id))
        data = json.loads(r.text)
        print(data['data']['replies'])
        if data['data']['replies'] is None:
            pass
        else:
            for i in data['data']['replies']:
                user_list.append(i['member']['uname'])
        pb.update_progress_bar(pg_num)

    set(user_list)
    tempdata = {'user': user_list}
    with open("Data\\data.json", 'w') as file_json:
        file_json.write(json.dumps(tempdata))
        file_json.close()


def getPageNum(av_id):
    r = requests.get('https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=1&oid={}&sort=2'.format(av_id))
    # 这个json地址获取方法：随便找一个评论用户的ID，在网页F12中CTRL+f 搜索 ，可以找到一个地址，复制地址，去掉callback回调部分
    data = json.loads(r.text)
    page_count = (data['data']['page']['count']) // 20 + 1  # 获取总页数，本来想用xpath直接爬到总页数，后来发现json里有个count总楼层数统计，所以可以计算出总页数

    return page_count


def getRandom(minNum, maxNum, count):
    Rum = set()
    while len(Rum) < count:
        Rum.add(random.randint(minNum, maxNum))

    Rum = list(Rum)
    return Rum
