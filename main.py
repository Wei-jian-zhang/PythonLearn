# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import Tk

import requests
import codecs
import json
import random
import time


class ProBar(object):
    """
    用于显示进度条！
    """
    _ProgrossBar: Tk

    def __init__(self, count):
        self.count = count
        self._ProgrossBar = Tk()
        self._ProgrossBar.title('正在获取评论区所有的用户，请稍候....')
        # 设置窗口居中
        # max_w:屏幕最大宽度,max_h:屏幕最大高度
        max_w, max_h = self._ProgrossBar.maxsize()
        # 窗口的宽度和高度
        wiw = 800
        wih = 200
        # 计算中心坐标
        cen_x = (max_w / 2) - (wiw / 2)
        cen_y = (max_h / 2) - (wih / 2)
        # 设置窗口大小和位置
        self._ProgrossBar.geometry('%dx%d+%d+%d' % (wiw, wih, cen_x, cen_y))
        self._ProgrossBar.resizable(False, False)
        self._ProgrossBar.config(bg='#535353')
        self.canvas_progress_bar = Canvas(self._ProgrossBar, width=630, height=20)
        self.canvas_shape = self.canvas_progress_bar.create_rectangle(0, 0, 0, 25, fill='green')
        self.canvas_text = self.canvas_progress_bar.create_text(292, 4, anchor=NW)
        self.canvas_progress_bar.itemconfig(self.canvas_text, text='00:00:00')
        self.var_progress_bar_percent = StringVar()
        self.var_progress_bar_percent.set('00.00  %')
        self.label_progress_bar_percent = Label(self._ProgrossBar, textvariable=self.var_progress_bar_percent,
                                                fg='#F5F5F5', bg='#535353')
        self.canvas_progress_bar.place(relx=0.45, rely=0.4, anchor=CENTER)
        self.label_progress_bar_percent.place(relx=0.89, rely=0.4, anchor=CENTER)
        # 按钮
        # self._ProgrossBar.mainloop()

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
            self._ProgrossBar.quit()
        else:
            pass
        self._ProgrossBar.update()


def av2bv(avid):
    site = "https://api.bilibili.com/x/web-interface/view?aid=" + str(avid)
    lst = codecs.decode(requests.get(site).content, "utf-8").split("\"")
    if int(lst[2][1:-1]) != 0: return 0
    return lst[13]


def bv2av(bvid):
    site = "https://api.bilibili.com/x/web-interface/view?bvid=" + bvid
    lst = codecs.decode(requests.get(site).content, "utf-8").split("\"")
    if int(lst[2][1:-1]) != 0: return 0
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
        pb.update_progress_bar(pg_num)
        r = requests.get(
            'https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn={}&type=1&oid={}&sort=2'.format(pg_num, av_id))
        data = json.loads(r.text)
        for i in data['data']['replies']:  # 每页有20层楼，遍历这20层楼获取ID
            user_list.append(i['member']['uname'])

    set(user_list)

    return user_list


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


if __name__ == '__main__':
    aid = bv2av("BV1PZ4y157rW")
    getAllcoment(aid)
    print('PyCharm')

