import pymysql
import time
import xlwt
import xlrd

def getConn():
    conn = pymysql.connect(
        host='localhost',
        user='jkw',
        passwd='123456',
        port=3306,
        db='shopping')
    return conn
    pass


def login():
    print('######登陆页面######')
    while True:
        username = input('用户名：')
        pwd = input('密码：')
        if username != '' and pwd != '':
            break
            pass
        print('用户名和密码不能为空')
        pass
    conn = getConn()
    cur = conn.cursor()
    sql1 = 'select * from user where username = "%s"' % (username)
    sql2 = 'select username from user'
    cur.execute(sql1)
    data1 = cur.fetchall()
    cur.execute(sql2)
    data2 = cur.fetchall()
    if (username, pwd) in data1:
        print('登陆成功')
        return username
        pass
    elif (username, ) not in data2:
        print('此用户不存在，请注册')
        register()
        pass
    else:
        print('用户名或密码不正确，请重新输入')
        login()
        pass


def register():
    print('######注册页面######')
    while True:
        username = input('用户名：')
        pwd = input('密码：')
        if username != '' and pwd != '':
            break
            pass
        print('用户名和密码不能为空')
        pass
    conn = getConn()
    cur = conn.cursor()
    sql1 = 'select username from user'
    cur.execute(sql1)
    data1 = cur.fetchall()
    if (username, ) in data1:
        print('此用户已存在，请重新输入')
        register()
        pass
    else:
        sql2 = 'insert into user(username,pwd) values("%s","%s")' % (username, pwd)
        row = cur.execute(sql2)
        if row == 1:
            print('注册成功，请登录')
            conn.commit()
            pass
        pass
    pass


def showAll():
    conn = getConn()
    cur = conn.cursor()
    sql1 = 'select * from goods'
    row1 = cur.execute(sql1)
    data1 = cur.fetchall()
    print('######商品列表######')
    for i in data1:
        print('编号：{} 名称：{} 种类：{} 价格：{} 库存：{}'.format(i[0], i[1], i[2], i[3], i[4]))
        pass
    pass


def showByKind():
    while True:
        kind = input('请输入要查看的商品的种类：')
        if kind != '':
            break
            pass
        print('商品种类不能为空')
        pass
    conn = getConn()
    cur = conn.cursor()
    sql1 = 'select * from goods where kind = "%s"' % (kind)
    row = cur.execute(sql1)
    data1 = cur.fetchall()
    if row > 0:
        print('######商品列表######')
        for i in data1:
            print('编号：{} 名称：{} 种类：{} 价格：{} 库存：{}'.format(i[0], i[1], i[2], i[3], i[4]))
            pass
        pass
    else:
        print('没有该种类的商品')
        pass
    pass


def insert():
    print('######添加商品页面######')
    while True:
        no = input('编号：')
        name = input('名称：')
        kind = input('种类：')
        if no != '' and name != '' and kind != '':
            break
            pass
        print('商品信息不能为空')
        pass
    while True:
        try:
            price = float(input('价格：'))
            stock = int(input('库存：'))
            break
            pass
        except Exception as e:
            print('请输入正确的数据')
            pass
        pass
    conn = getConn()
    cur = conn.cursor()
    sql1 = 'select * from goods where no = "%s"' % (no)
    row1 = cur.execute(sql1)
    if row1 == 1:
        print('此商品已存在')
        pass
    else:
        sql2 = 'insert into goods values("%s","%s","%s",%f,%d)' % (no, name, kind, price, stock)
        row2 = cur.execute(sql2)
        if row2 == 1:
            print('添加成功')
            pass
        else:
            print('添加失败')
            pass
        conn.commit()
        pass
    pass


def update():
    print('######修改商品页面######')
    print('请输入要修改的商品的编号')
    while True:
        no = input('编号：')
        if no != '':
            break
            pass
        print('编号不能为空')
        pass
    conn = getConn()
    cur = conn.cursor()
    sql1 = 'select * from goods where no = "%s"' % (no)
    row1 = cur.execute(sql1)
    data1 = cur.fetchall()
    if row1 == 0:
        print('该商品不存在，请重新输入')
        update()
        pass
    else:
        print('该商品当前信息如下：')
        for i in data1:
            print('编号：{} 名称：{} 种类：{} 价格：{} 库存：{}'.format(i[0], i[1], i[2], i[3], i[4]))
            pass
        while True:
            print('请输入要修改的属性 编号/名称/种类/价格/库存')
            opt = input('属性：')
            print('请输入修改后的"%s"' % (opt))
            while True:
                val1 = input('"%s"：' % (opt))
                if val1 != '':
                    break
                    pass
                print('"%s"不能为空' % (opt))
                pass
            if opt == "编号":
                sql2 = 'update goods set no = "%s" where no = "%s"' % (val1, no)
                pass
            elif opt == "名称":
                sql2 = 'update goods set name = "%s" where no = "%s"' % (val1, no)
                pass
            elif opt == "种类":
                sql2 = 'update goods set kind = "%s" where no = "%s"' % (val1, no)
                pass
            elif opt == "价格":
                while True:
                    try:
                        val2 = float(val1)
                        break
                        pass
                    except Exception as e:
                        print('请输入正确的数据')
                        pass
                    pass
                sql2 = 'update goods set price = %f where no = "%s"' % (val2, no)
                pass
            elif opt == "库存":
                while True:
                    try:
                        val2 = int(val1)
                        break
                        pass
                    except Exception as e:
                        print('请输入正确的数据')
                        pass
                    pass
                sql2 = 'update goods set stock = %d where no = "%s"' % (val2, no)
                pass
            else:
                print('请输入正确的属性')
                continue
                pass
            row2 = cur.execute(sql2)
            if row2 == 1:
                print('修改成功')
                pass
            else:
                print('修改失败')
                pass
            conn.commit()
            break
            pass
        pass
    pass


def delete():
    print('######删除商品页面######')
    print('请输入要删除的商品的编号')
    while True:
        no = input('编号：')
        if no != '':
            break
            pass
        print('编号不能为空')
        pass
    conn = getConn()
    cur = conn.cursor()
    sql1 = 'select * from goods where no = "%s"' % (no)
    row1 = cur.execute(sql1)
    data1 = cur.fetchall()
    if row1 == 0:
        print('该商品不存在，请重新输入')
        delete()
        pass
    else:
        print('该商品当前信息如下：')
        for i in data1:
            print('编号：{} 名称：{} 种类：{} 价格：{} 库存：{}'.format(i[0], i[1], i[2], i[3], i[4]))
            pass
        while True:
            opt = input('是否删除该商品？ Y/N ：')
            if opt == 'Y':
                sql2 = 'delete from goods where no = "%s"' % (no)
                row2 = cur.execute(sql2)
                if row2 == 1:
                    print('删除成功')
                    pass
                else:
                    print('删除失败')
                    pass
                conn.commit()
                pass
            elif opt != 'Y' and opt != 'N':
                print('请输入Y/N')
                continue
                pass
            break
            pass
        pass
    pass


def shop(username):
    print('######购买商品页面######')
    showAll()
    print('请输入要购买的商品的编号')
    while True:
        no = input('编号：')
        if no != '':
            break
            pass
        print('编号不能为空')
        pass
    conn = getConn()
    cur = conn.cursor()
    sql1 = 'select * from goods where no = "%s"' % (no)
    row1 = cur.execute(sql1)
    data1 = cur.fetchall()
    if row1 == 0:
        print('该商品不存在，请重新输入')
        shop(username)
        pass
    else:
        print('该商品当前信息如下：')
        for i in data1:
            print('编号：{} 名称：{} 种类：{} 价格：{} 库存：{}'.format(i[0], i[1], i[2], i[3], i[4]))
            pass
        while True:
            print('请输入购买数量')
            while True:
                try:
                    num = int(input('数量：'))
                    break
                    pass
                except Exception as e:
                    print('请输入正确的数据')
                    pass
                pass
            sql2 = 'select stock from goods where no = "%s"' % (no)
            cur.execute(sql2)
            data2 = cur.fetchall()
            if num > data2[0][0]:
                print('库存不足，请重新输入')
                continue
                pass
            else:
                sql3 = 'select price from goods where no = "%s"' % (no)
                cur.execute(sql3)
                data3 = cur.fetchall()
                allprice = num * data3[0][0]
                print('购买成功')
                print('购买商品信息如下：')
                print('编号：{} 数量：{} 单价：{} 总价：{}'.format(no, num, data3[0][0], allprice))
                stock_o = data2[0][0] - num
                sql4 = 'update goods set stock = %d where no = "%s"' % (stock_o, no)
                cur.execute(sql4)
                time1 = time.strftime("%Y-%m-%d %H:%M:%S")
                sql5 = 'insert into shopping values("%s","%s",%f,"%d",%f,"%s","%s")' % (no, data1[0][1], data3[0][0], num, allprice, time1, username)
                cur.execute(sql5)
                conn.commit()
                break
                pass
            pass
        pass
    while True:
        opt = input('是否继续购买 Y/N：')
        if opt == 'Y':
            shop(username)
            pass
        elif opt != 'Y' and opt != 'N':
            print('请输入Y/N')
            continue
            pass
        break
        pass
    pass


def endshopping(username):
    conn = getConn()
    cur = conn.cursor()
    sql1 = 'select no,name,price,num,allprice,time from shopping where username = "%s"'%(username)
    cur.execute(sql1)
    data1 = cur.fetchall()
    print('######购物单######')
    cost = 0
    for i in data1:
        print('编号：{} 名称：{} 单价：{} 数量：{} 总价：{} 时间：{}'.format(i[0], i[1], i[2], i[3], i[4], i[5]))
        cost = cost + i[4]
        pass
    print('{}用户\t你本次共消费{}元'.format(username,cost))
    sql2 = 'delete from shopping where username = "%s"'%(username)
    cur.execute(sql2)
    conn.commit()
    pass


def export(outputpath):
    conn = getConn()
    cur = conn.cursor()
    count = cur.execute('select * from goods')
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
    workbook.save(outputpath)
    print('导出成功')
    pass


def main():
    while True:
        print('------欢迎光临教育超市------')
        print('1、登陆 2、注册 3、退出')
        opt1 = input('请输入选项：')
        if opt1 == '1':
            username = login()
            break
            pass
        elif opt1 == '2':
            register()
            continue
            pass
        elif opt1 == '3':
            break
            pass
        else:
            print('输入有误，请重新输入')
            continue
            pass
        pass
    print('欢迎{}登录'.format(username))
    while True: 
        print('######购物页面######')
        print('1、查看所有商品 2、根据商品种类查看商品 3、添加商品 4、修改商品 5、删除商品 6、购买商品 7、导出所有商品信息 8、退出')
        opt2 = input('请输入选项：')
        if opt2 == '1':
            showAll()
            pass
        elif opt2 == '2':
            showByKind()
            pass
        elif opt2 == '3':
            insert()
            pass
        elif opt2 == '4':
            update()
            pass
        elif opt2 == '5':
            delete()
            pass
        elif opt2 == '6':
            shop(username)
            pass
        elif opt2 == '7':
            export('E:/Python/Forth/goods.xls')
            pass
        elif opt2 == '8':
            endshopping(username)
            break
            pass
        else:
            print('输入有误，请重新输入')
            continue
            pass
        pass
    pass


if __name__ == "__main__":
    main()
    pass