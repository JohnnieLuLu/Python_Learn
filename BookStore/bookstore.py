import tkinter
import tkinter.ttk
import tkinter.messagebox
from tkinter import *
import xlwt
import time
import pymysql
import sys
import re

def center(root, width, height):
    x = root.winfo_screenwidth()
    y = root.winfo_screenheight()
    size = '%dx%d+%d+%d' % (width, height, (x - width) / 2, (y - height) / 2)
    root.geometry(size)
    pass

def getConn():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        passwd='123456',
        port=3306,
        db='bookstore')
    return conn

def statement():
    m1 = tkinter.messagebox.showinfo(title='提示', message='谢谢支持')
    pass

def typeadd(frame1):
    def add():
        tid = e1.get()
        tname = e2.get()
        conn = getConn()
        cur = conn.cursor()
        if tid == '' or tname == '':
            tkinter.messagebox.showinfo(title='错误', message='内容不能为空')
            pass
        else:
            sql1 = 'select * from booktype where tid ="%s"' % (tname)
            row1 = cur.execute(sql1)
            if row1 == 1:
                tkinter.messagebox.showinfo(title='错误', message='该类别已存在')
                pass
            else:
                sql2 = 'insert into booktype(tid,tname) values("%s","%s")' % (tid,tname)
                row2 = cur.execute(sql2)
                data = cur.fetchall()
                if row2 == 1:
                    tkinter.messagebox.showinfo(title='提示', message='添加成功')
                    conn.commit()
                    root.destroy()
                    typeselect(frame1)
                    pass
                else:
                    tkinter.messagebox.showinfo(title='提示', message='添加失败')
                    pass
                pass
            pass
        pass

    typeselect(frame1)
    root = tkinter.Tk()
    root.title('添加图书类别')
    center(root, 300, 300)
    f1 = LabelFrame(root, text='图书类别信息:')
    f1.pack(pady=70)
    l1 = Label(f1, text='编号')
    l1.grid(row=0, column=0, padx=20, pady=10, sticky=W)
    e1 = Entry(f1)
    e1.grid(row=0, column=1, padx=20, pady=10)
    l2 = Label(f1, text='类别名')
    l2.grid(row=1, column=0, padx=20, pady=10, sticky=W)
    e2 = Entry(f1)
    e2.grid(row=1, column=1, padx=20, pady=10)
    f2 = LabelFrame(root)
    f2.pack()
    b1 = Button(f2, text='添加', command=add)
    b1.pack(padx=20, pady=10)
    root.mainloop()
    pass

def typedel(frame1):
    def delete(e):
        tid = e.get()
        conn = getConn()
        cur = conn.cursor()
        if tid == '':
            tkinter.messagebox.showinfo(title='提示', message='编号不能为空')
            pass
        else:
            sql1 = 'select * from booktype where tid =%s' % (tid)
            row1 = cur.execute(sql1)
            if row1 == 0:
                tkinter.messagebox.showinfo(title='提示', message='该编号不存在')
                pass
            else:
                sql2 = 'select * from bookinfo where tid =%s' % (tid)
                row2 = cur.execute(sql2)
                if row2 != 0:
                    tkinter.messagebox.showinfo(
                        title='提示', message='该编号的图书已存在，请先删除类型编号为%s的图书' % (tid))
                    pass
                else:
                    sql3 = 'delete from booktype where tid = %s' % (tid)
                    row3 = cur.execute(sql3)
                    if row3 == 1:
                        tkinter.messagebox.showinfo(title='提示', message='删除成功')
                        root.destroy()
                        conn.commit()
                        typeselect(frame1)
                        pass
                    else:
                        tkinter.messagebox.showinfo(title='提示', message='删除失败')
                        pass
                    pass
                pass
            pass
        pass

    typeselect(frame1)
    root = tkinter.Tk()
    root.title('删除图书种类信息')
    center(root, 300, 300)
    frame = LabelFrame(root, text='请输入要删除的类别编号')
    frame.pack()
    e = Entry(frame)
    e.grid(row=0, column=0, padx=20, pady=20)
    btn = Button(frame, text='删除', command=lambda:delete(e))
    btn.grid(row=0, column=1, padx=20, pady=20)
    root.mainloop()
    pass


def typeupdate(frame1):
    def update(e1,e2):
        tid = e1.get()
        tname = e2.get()
        pass
        conn = getConn()
        cur = conn.cursor()
        if tid == '' or tname == '':
            tkinter.messagebox.showinfo(title='提示', message='输入数据不能为空')
            pass
        else:
            sql1 = 'select * from booktype where tid =%s' % (tid)
            row1 = cur.execute(sql1)
            if row1 == 0:
                tkinter.messagebox.showinfo(title='提示', message='该类型不存在')
                pass
            else:
                sql2 = 'update booktype set tname = "%s" where tid = %s' % (tname, tid)
                row2 = cur.execute(sql2)
                if row2 == 1:
                    m1 = tkinter.messagebox.showinfo(title='提示', message='修改成功')
                    conn.commit()
                    root.destroy()
                    typeselect(frame1)
                    pass
                else:
                    m2 = tkinter.messagebox.showinfo(title='提示', message='修改失败')
                    pass
                pass
            pass
        pass

    typeselect(frame1)

    root = tkinter.Tk()
    root.title('修改图书种类信息')
    center(root, 300, 300)
    frame = LabelFrame(root, text='请输入要修改的种类编号及修改后的种类名')
    frame.pack()
    lab1 = Label(frame, text='编号')
    e1 = Entry(frame)
    lab2 = Label(frame, text='类别名')
    e2 = Entry(frame)
    btn = Button(frame, text='修改', command=lambda:update(e1,e2))
    lab1.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    e1.grid(row=0, column=1, padx=10, pady=10)
    lab2.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    e2.grid(row=1, column=1, padx=10, pady=10)
    btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    root.mainloop()
    pass

#查询
def typeselect(frame1):
    conn = getConn()
    cur = conn.cursor()
    sql = 'select * from booktype'
    row = cur.execute(sql)
    data = cur.fetchall()
    for widget in frame1.winfo_children():
        widget.destroy()
        pass
    tree = tkinter.ttk.Treeview(frame1, columns=['1', '2'], show='headings')
    tree.column('1', width=225, anchor='center')
    tree.column('2', width=225, anchor='center')
    tree.heading('1', text='tid')
    tree.heading('2', text='tname')
    for i in data:
        tree.insert('', 'end', values=(i[0], i[1]))
        pass
    tree.grid()
    pass


def bookadd(frame1):
    def add(e1,e2,e3,e4,e5):
        bid = e1.get()
        bname = e2.get()
        bprice = float(e3.get())
        tid = e4.get()
        bcount = int(e5.get())
        conn = getConn()
        cur = conn.cursor()
        if bid == '' or bname == '' or bprice == '' or tid == '' or bcount == '':
            tkinter.messagebox.showinfo(title='提示', message='输入数据不能为空')
            pass
        else:
            sql1 = 'select * from bookinfo where bid = "%s"' % (bid)
            row1 = cur.execute(sql1)
            if row1 == 1:
                tkinter.messagebox.showinfo(title='提示', message='该图书已存在')
                pass
            else:
                sql2 = 'select * from booktype where tid = %s' % (tid)
                row2 = cur.execute(sql2)
                if row2 == 0:
                    tkinter.messagebox.showinfo(title='提示', message='该类别不存在')
                    pass
                else:
                    sql3 = 'insert into bookinfo(bid,bname,bprice,tid,bcount) values("%s","%s",%f,"%s",%d)' % (bid,bname, 
                    bprice, tid, bcount)
                    row3 = cur.execute(sql3)
                    data = cur.fetchall()
                    if row3 == 1:
                        tkinter.messagebox.showinfo(title='提示', message='添加成功')
                        conn.commit()
                        root.destroy()
                        bookselect(frame1)
                        pass
                    else:
                        tkinter.messagebox.showinfo(title='提示', message='添加失败')
                        pass
                    pass
                pass
            pass
        pass

    bookselect(frame1)

    root = tkinter.Tk()
    root.title('添加图书')
    center(root, 300, 300)
    frame = LabelFrame(root, text='添加')
    frame.pack()
    v1 = StringVar()
    v2 = StringVar()
    v3 = StringVar()
    lab1 = Label(frame, text='bid')
    e1 = Entry(frame)
    lab2 = Label(frame, text='bname')
    e2 = Entry(frame)
    lab3 = Label(frame, text='bprice')
    e3 = Entry(frame)
    lab4 = Label(frame, text='tid')
    e4 = Entry(frame)
    lab5 = Label(frame, text='bcount')
    e5 = Entry(frame)
    btn = Button(frame, text='添加', command=lambda:add(e1,e2,e3,e4,e5))
    lab1.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    e1.grid(row=0, column=1, padx=10, pady=10)
    lab2.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    e2.grid(row=1, column=1, padx=10, pady=10)
    lab3.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    e3.grid(row=2, column=1, padx=10, pady=10)
    lab4.grid(row=3, column=0, padx=10, pady=10, sticky=W)
    e4.grid(row=3, column=1, padx=10, pady=10)
    lab5.grid(row=4, column=0, padx=10, pady=10, sticky=W)
    e5.grid(row=4, column=1, padx=10, pady=10)
    btn.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    root.mainloop()
    pass


def bookdel(frame1):
    def delete(e):
        bid = e.get()
        conn = getConn()
        cur = conn.cursor()
        if bid == '':
            tkinter.messagebox.showinfo(title='提示', message='输入数据不能为空')
            pass
        else:
            sql1 = 'select * from bookinfo where bid = %s' % (bid)
            row1 = cur.execute(sql1)
            if row1 == 0:
                m1 = tkinter.messagebox.showinfo(title='提示', message='该书不存在')
                pass
            else:
                sql2 = 'delete from bookinfo where bid = %s' % (bid)
                row2 = cur.execute(sql2)
                if row2 == 1:
                    tkinter.messagebox.showinfo(title='提示', message='删除成功')
                    root.destroy()
                    conn.commit()
                    bookselect(frame1)
                    pass
                else:
                    tkinter.messagebox.showinfo(title='提示', message='删除失败')
                    pass
                pass
            pass
        pass

    bookselect(frame1)

    root = tkinter.Tk()
    root.title('删除图书')
    center(root, 300, 300)
    frame = LabelFrame(root, text='请输入要删除的图书编号')
    frame.pack()
    e = Entry(frame)
    e.grid(row=0, column=0, padx=20, pady=20)
    btn = Button(frame, text='删除', command=lambda:delete(e))
    btn.grid(row=0, column=1, padx=20, pady=20)
    root.mainloop()
    pass


def bookupdate(frame1):
    def update(e1,e2,e3,e4,e5):
        bid = e1.get()
        bname = e2.get()
        bprice = float(e3.get())
        tid = e4.get()
        bcount = int(e5.get())
        conn = getConn()
        cur = conn.cursor()
        if bid == '' or bname == '' or bprice == '' or tid == '' or bcount == '' or bid == '':
            tkinter.messagebox.showinfo(title='提示', message='输入数据不能为空')
            pass
        else:
            sql1 = 'select * from bookinfo where bid = %s' % (bid)
            row1 = cur.execute(sql1)
            if row1 == 0:
                tkinter.messagebox.showinfo(title='提示', message='该图书不存在')
                pass
            else:
                sql2 = 'update bookinfo set bname="%s",bprice=%f,tid=%s,bcount=%d where bid = %s' % (bname, bprice, 
                tid, bcount, bid)
                row2 = cur.execute(sql2)
                if row2 == 1:
                    m1 = tkinter.messagebox.showinfo(title='提示', message='修改成功')
                    conn.commit()
                    root.destroy()
                    bookselect(frame1)
                    pass
                else:
                    m2 = tkinter.messagebox.showinfo(title='提示', message='修改失败')
                    pass
                pass
            pass
        pass

    bookselect(frame1)

    root = tkinter.Tk()
    root.title('修改图书信息')
    center(root, 300, 300)
    frame = LabelFrame(root, text='请输入要修改的图书编号及修改后的图书信息')
    frame.pack()
    lab1 = Label(frame, text='bid')
    e1 = Entry(frame)
    lab2 = Label(frame, text='bname')
    e2 = Entry(frame)
    lab3 = Label(frame, text='bprice')
    e3 = Entry(frame)
    lab4 = Label(frame, text='tid')
    e4 = Entry(frame)
    lab5 = Label(frame, text='bcount')
    e5 = Entry(frame)
    btn = Button(frame, text='修改', command=lambda:update(e1,e2,e3,e4,e5))
    lab1.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    e1.grid(row=0, column=1, padx=10, pady=10)
    lab2.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    e2.grid(row=1, column=1, padx=10, pady=10)
    lab3.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    e3.grid(row=2, column=1, padx=10, pady=10)
    lab4.grid(row=3, column=0, padx=10, pady=10, sticky=W)
    e4.grid(row=3, column=1, padx=10, pady=10)
    lab5.grid(row=4, column=0, padx=10, pady=10, sticky=W)
    e5.grid(row=4, column=1, padx=10, pady=10)
    btn.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
    root.mainloop()
    pass


def bookselect(frame1):
    conn = getConn()
    cur = conn.cursor()
    sql = 'select * from bookinfo'
    row = cur.execute(sql)
    data = cur.fetchall()
    for widget in frame1.winfo_children():
        widget.destroy()
        pass
    tree = tkinter.ttk.Treeview(
        frame1, columns=['1', '2', '3', '4', '5'], show='headings')
    tree.column('1', width=90, anchor='center')
    tree.column('2', width=90, anchor='center')
    tree.column('3', width=90, anchor='center')
    tree.column('4', width=90, anchor='center')
    tree.column('5', width=90, anchor='center')
    tree.heading('1', text='bid')
    tree.heading('2', text='bname')
    tree.heading('3', text='bprice')
    tree.heading('4', text='tid')
    tree.heading('5', text='bcount')
    for i in data:
        tree.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4]))
        pass
    tree.grid()
    pass


def export():
    conn = getConn()
    cur = conn.cursor()
    count = cur.execute('select * from bookinfo')
    cur.scroll(0, mode='absolute')
    results = cur.fetchall()
    fields = cur.description
    workbook = xlwt.Workbook()
    sheet = workbook.add_sheet('sheet1', cell_overwrite_ok=True)
    for field in range(0, len(fields)):
        sheet.write(0, field, fields[field][0])
        pass
    row = 1
    col = 0
    for row in range(1, len(results) + 1):
        for col in range(0, len(fields)):
            sheet.write(row, col, u'%s' % results[row - 1][col])
            pass
        pass
    workbook.save('E:/Python/Fifth/book.xls')
    tkinter.messagebox.showinfo(title='提示', message='导出成功')
    pass


def bookbuy(username, frame1):
    def buy(e1,e2):
        bid = e1.get()
        count = int(e2.get())
        conn = getConn()
        cur = conn.cursor()
        if bid == '' or count == '':
            tkinter.messagebox.showinfo(title='提示', message='输入数据不能为空')
            pass
        else:
            sql1 = 'select bname,bprice,bcount from bookinfo where bid = %s' % (bid)
            row1 = cur.execute(sql1)
            data1 = cur.fetchall()
            if row1 == 0:
                tkinter.messagebox.showinfo(title='提示', message='该图书不存在')
                pass
            else:
                bname = data1[0][0]
                bprice = data1[0][1]
                bcount = data1[0][2]
                if count > bcount:
                    tkinter.messagebox.showinfo(title='提示', message='该图书库存不足')
                    pass
                else:
                    sql2 = 'update bookinfo set bcount=%d where bid = %s' % (
                        bcount - count, bid)
                    row2 = cur.execute(sql2)
                    allprice = count * bprice
                    sql3 = 'insert into buy(bname,bprice,count,allprice,username) values("%s",%f,%d,%f,"%s")' % (bname, 
                    bprice, count, allprice, username)
                    row3 = cur.execute(sql3)
                    if row3 >= 1:
                        tkinter.messagebox.showinfo(title='提示', message='购买成功')
                        conn.commit()
                        root.destroy()
                        bookselect(frame1)
                        pass
                    else:
                        tkinter.messagebox.showinfo(title='提示', message='购买失败')
                        pass
                    pass
                pass
            pass
        pass

    bookselect(frame1)
    root = tkinter.Tk()
    root.title('图书购买')
    center(root, 300, 300)
    frame = LabelFrame(root, text='请输入要购买的图书的编号及数量')
    frame.pack()
    lab1 = Label(frame, text='图书编号')
    e1 = Entry(frame)
    lab2 = Label(frame, text='数量')
    e2 = Entry(frame)
    btn = Button(frame, text='购买', command=lambda:buy(e1,e2))
    lab1.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    e1.grid(row=0, column=1, padx=10, pady=10)
    lab2.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    e2.grid(row=1, column=1, padx=10, pady=10)
    btn.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
    root.mainloop()
    pass


def pay(username, frame1):
    conn = getConn()
    cur = conn.cursor()
    sql = 'select * from buy'
    row = cur.execute(sql)
    data = cur.fetchall()
    for widget in frame1.winfo_children():
        widget.destroy()
        pass
    tree = tkinter.ttk.Treeview(
        frame1, columns=['1', '2', '3', '4', '5'], show='headings')
    tree.column('1', width=75, anchor='center')
    tree.column('2', width=75, anchor='center')
    tree.column('3', width=75, anchor='center')
    tree.column('4', width=75, anchor='center')
    tree.column('5', width=75, anchor='center')
    tree.heading('1', text='bname')
    tree.heading('2', text='bprice')
    tree.heading('3', text='count')
    tree.heading('4', text='allprice')
    tree.heading('5', text='username')
    for i in data:
        tree.insert('', 'end', values=(i[0], i[1], i[2], i[3], i[4]))
        pass
    tree.grid()
    sql2 = 'select allprice from buy'
    row2 = cur.execute(sql2)
    data2 = cur.fetchall()
    cost = 0
    for i in data2:
        cost = cost + i[0]
        pass
    lab = Label(frame1, text='')
    lab['text'] = '你一共消费%.2f元' % (cost)
    lab.grid()
    sql3 = 'delete from buy where username = "%s"' % (username)
    row3 = cur.execute(sql3)
    conn.commit()
    pass


def index():
    def tologin():
        root.destroy()
        loginframe()
        pass

    def toregister():
        root.destroy()
        registerframe()
        pass

    root = tkinter.Tk()
    root.title('首页')
    center(root, 400, 400)
    f1 = Frame(root, width=300, height=200)
    f1.pack_propagate(0)
    f1.pack(side=TOP, pady=20)
    l1 = Label(f1, text='后钝书店', font=('宋体', 50), fg='red')
    l1.pack(anchor=CENTER, pady=20)
    f2 = Frame(root)
    f2.pack()
    b1 = Button(f2, text='登陆', command=tologin)
    b1.grid(row=0, column=0, padx=20, pady=20)
    b2 = Button(f2, text='注册', command=toregister)
    b2.grid(row=0, column=1, padx=20, pady=20)
    root.mainloop()
    pass


def registerframe():
    def reset():
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        v.set(1)
        e4.delete(0, END)
        e5.delete(0, END)
        pass

    def register():
        username = e1.get()
        password = e2.get()
        name = e3.get()
        mail = e4.get()
        tel = e5.get()
        gender = ''
        if v.get() == 1:
            gender = '男'
            pass
        if v.get() == 2:
            gender = '女'
            pass
        if username == '' or password == '' or name == '' or mail == '' or tel == '':
            m1 = tkinter.messagebox.showinfo(title='提示', message='有空数据，请重新输入')
            pass
        else:
            conn = getConn()
            cur = conn.cursor()
            sql1 = 'insert into userinfo(username,password,name,gender,mail,tel) values("%s","%s","%s","%s","%s","%s")' % (
                username, password, name, gender, mail, tel)
            sql2 = 'insert into user(username,password) values("%s","%s")' % (
                username, password)
            row = cur.execute(sql1)
            cur.execute(sql2)
            if row == 1:
                tkinter.messagebox.showinfo(title='提示', message='注册成功')
                conn.commit()
                root.destroy()
                loginframe()
                pass
            else:
                tkinter.messagebox.showinfo(title='提示', message='注册失败')
                pass
            pass
        pass

    def validate_tel(value):
        if not re.search('^1[0-9]{10}$', str(value)):
            tkinter.messagebox.showinfo(title='提示', message='手机号不正确')
        return True
        pass

    def validate_mail(value):
        if not re.search('\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*',
                         str(value)):
            tkinter.messagebox.showinfo(title='提示', message='邮箱格式不正确')
        return True
        pass

    root = tkinter.Tk()
    root.title('注册界面')
    center(root, 400, 400)
    testmobile = root.register(validate_tel)
    testemail = root.register(validate_mail)
    f1 = Frame(root)
    f1.pack(pady=20)
    lab1 = Label(f1, text='用户名')
    lab1.grid(row=0, column=0, padx=10, pady=10, sticky=W)
    e1 = Entry(f1)
    e1.grid(row=0, column=1, columnspan=2, padx=10, pady=10)
    lab2 = Label(f1, text='密码')
    lab2.grid(row=1, column=0, padx=10, pady=10, sticky=W)
    e2 = Entry(f1)
    e2.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
    lab3 = Label(f1, text='真实姓名')
    lab3.grid(row=2, column=0, padx=10, pady=10, sticky=W)
    e3 = Entry(f1)
    e3.grid(row=2, column=1, columnspan=2, padx=10, pady=10)
    lab4 = Label(f1, text='性别')
    lab4.grid(row=3, column=0, padx=10, pady=10, sticky=W)
    v = IntVar()
    v.set(1)
    rb1 = Radiobutton(f1, variable=v, text='男', value=1)
    rb1.grid(row=3, column=1, padx=10, pady=10)
    rb2 = Radiobutton(f1, variable=v, text='女', value=2)
    rb2.grid(row=3, column=2, padx=10, pady=10)
    v1 = StringVar()
    v2 = StringVar()
    lab5 = Label(f1, text='邮箱')
    lab5.grid(row=4, column=0, padx=10, pady=10, sticky=W)
    e4 = Entry(
        f1,
        textvariable=v1,
        validate='focusout',
        validatecommand=(testemail, '%P'))
    e4.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
    lab6 = Label(f1, text='电话')
    lab6.grid(row=5, column=0, padx=10, pady=10, sticky=W)
    e5 = Entry(
        f1,
        textvariable=v2,
        validate='focusout',
        validatecommand=(testmobile, '%P'))
    e5.grid(row=5, column=1, columnspan=2, padx=10, pady=10)
    f2 = Frame(root)
    f2.pack()
    btn1 = Button(f2, text='注册', command=register)
    btn1.grid(row=0, column=0, padx=10)
    btn2 = Button(f2, text='重置', command=reset)
    btn2.grid(row=0, column=1, padx=10)
    btn3 = Button(f2, text='退出', command=sys.exit)
    btn3.grid(row=0, column=2, padx=10)
    root.mainloop()
    pass


def loginframe():
    def reset():
        e1.delete(0, END)
        e2.delete(0, END)
        pass

    def login():
        username = e1.get()
        password = e2.get()
        if username == '' or password == '':
            m1 = tkinter.messagebox.showinfo(title='提示', message='有空数据，请重新输入')
            pass
        else:
            conn = getConn()
            cur = conn.cursor()
            sql = 'select * from user where username = "%s"' % (username)
            row = cur.execute(sql)
            if row == 0:
                m1 = tkinter.messagebox.showinfo(title='提示', message='此用户不存在，请注册')
                root.destroy()
                registerframe()
                pass
            else:
                sql = 'select * from user where username = "%s" and password = "%s"' % (username, password)
                row = cur.execute(sql)
                data = cur.fetchall()
                if row == 1:
                    root.destroy()
                    mainpage(username)
                    pass
                else:
                    m1 = tkinter.messagebox.showinfo(title='提示', message='用户名与密码不匹配')
                    pass
                pass
            pass
        pass

    root = tkinter.Tk()
    root.title('登录界面')
    center(root, 400, 300)
    f1 = Frame(root)
    f1.pack(pady=40)
    l1 = Label(f1, text='用户名')
    l1.grid(row=0, column=0, padx=20, pady=20, sticky=W)
    e1 = Entry(f1)
    e1.grid(row=0, column=1, padx=20, pady=20)
    l2 = Label(f1, text='密码')
    l2.grid(row=1, column=0, padx=20, pady=20, sticky=W)
    e2 = Entry(f1, show='*')
    e2.grid(row=1, column=1, padx=20, pady=20)
    f2 = Frame(root)
    f2.pack()
    b1 = Button(f2, text='登录', command=login)
    b1.grid(row=0, column=0, padx=20, pady=10)
    b2 = Button(f2, text='重置', command=reset)
    b2.grid(row=0, column=1, padx=20, pady=10)
    b3 = Button(f2, text='退出', command=sys.exit)
    b3.grid(row=0, column=2, padx=20, pady=10)
    root.mainloop()
    pass


def mainpage(username):
    root = tkinter.Tk()
    root.title('主界面')
    center(root, 450, 300)
    frame1 = Frame(root)
    frame1.pack()
    menu = Menu(root)
    typemenu = Menu(menu, tearoff=False)
    typemenu.add_command(label='增加', command=lambda: typeadd(frame1))
    typemenu.add_command(label='删除', command=lambda: typedel(frame1))
    typemenu.add_command(label='修改', command=lambda: typeupdate(frame1))
    typemenu.add_command(label='查询', command=lambda: typeselect(frame1))
    typemenu.add_separator()
    menu.add_cascade(label='类别', menu=typemenu)
    bookmenu = Menu(menu, tearoff=False)
    bookmenu.add_command(label='增加', command=lambda: bookadd(frame1))
    bookmenu.add_command(label='删除', command=lambda: bookdel(frame1))
    bookmenu.add_command(label='修改', command=lambda: bookupdate(frame1))
    bookmenu.add_command(label='查询', command=lambda: bookselect(frame1))
    bookmenu.add_command(label='导出', command=export)
    bookmenu.add_separator()
    menu.add_cascade(label='书信息', menu=bookmenu)
    aboutmenu = Menu(menu, tearoff=False)
    aboutmenu.add_command(label='关于我们', command=statement)
    aboutmenu.add_separator()
    menu.add_cascade(label='关于我们', menu=aboutmenu)
    helpmenu = Menu(menu, tearoff=False)
    helpmenu.add_command(label='帮助', command=statement)
    helpmenu.add_separator()
    menu.add_cascade(label='帮助', menu=helpmenu)
    buymenu = Menu(menu, tearoff=False)
    buymenu.add_command(label='购买', command=lambda: bookbuy(username, frame1))
    buymenu.add_command(label='结算', command=lambda: pay(username, frame1))
    buymenu.add_separator()
    buymenu.add_command(label='退出', command=sys.exit)
    menu.add_cascade(label='购买图书', menu=buymenu)
    root.config(menu=menu)
    root.mainloop()
    pass

if __name__ == "__main__":
    index()
    pass