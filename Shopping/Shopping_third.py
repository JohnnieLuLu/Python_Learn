#coding
import sys
import os

class Shopping(object):
    @staticmethod
    def login():
        print('*******登陆页面*******')
        username = input('用户名：')
        pwd = input('密码：')

        users = []
        usernames = []
        try:
            f = open('E:/Python/Third/user.txt','r',encoding='UTF-8')
        except FileNotFoundError:
            os.mknod('E:/Python/Third/user.txt')
        
        for lines in f.readlines():
            lines=lines.replace('\n','').split('#')
            users.append(lines)
            usernames.append(lines[0])
        pass
        f.close()

        if [username,pwd] in users:
            print('登陆成功')
            pass
        elif username not in usernames:
            print('此用户不存在，请注册')
            Shopping.register()
            pass
        else:
            print('用户名或密码不正确，请重新输入')
            Shopping.login()
            pass


    @staticmethod
    def register():
        print('*******注册页面*******')
        username = input('用户名：')
        pwd = input('密码：')

        usernames = []
        f = open('E:/Python/Third/user.txt','r',encoding='UTF-8')
        for lines in f.readlines():
            lines=lines.replace('\n','').split('#')
            usernames.append(lines[0])
            pass
        f.close()

        if username not in usernames:
            f1 = open('E:/Python/Third/user.txt','a',encoding='UTF-8')
            f1.write(username+'#'+pwd+'\n')
            f1.close()
            print('注册成功，请登录')
            Shopping.login()
            pass
        else:
            print('此用户已存在，请重新输入')
            Shopping.register()
        pass

    @staticmethod
    def showAll():
        print('*******商品列表*******')
        print('编号\t\t名称\t\t种类\t\t价格\t\t库存')

        f = open('E:/Python/Third/goods.txt','r',encoding='UTF-8')
        for lines in f.readlines():
            lines=lines.replace('\n','').split('#')
            print(lines[0]+'\t\t'+lines[1]+'\t\t'+lines[2]+'\t\t'+lines[3]+'\t\t'+lines[4])
            pass
        f.close()
        pass
    
    @staticmethod
    def showByKind():
        kind = input('请输入要查看的商品的种类：')
        print('*******商品列表*******')
        print('编号\t\t名称\t\t种类\t\t价格\t\t库存')

        f = open('E:/Python/Third/goods.txt','r',encoding='UTF-8')
        for lines in f.readlines():
            lines=lines.replace('\n','').split('#')
            print(lines[0]+'\t\t'+lines[1]+'\t\t'+lines[2]+'\t\t'+lines[3]+'\t\t'+lines[4])
            pass
        f.close()
        pass

    @staticmethod
    def insert():
        print('*******添加商品*******')
        no = input('编号：')
        name = input('名称：')
        kind = input('种类：')
        price = input('价格：')
        stock = input('库存：')
        
        nos = []
        f = open('E:/Python/Third/goods.txt','r',encoding='UTF-8')
        for lines in f.readlines():
            lines=lines.replace('\n','').split('#')
            nos.append(lines[0])
            pass
        f.close()

        if no in nos:
            print('此商品已存在，请重新输入')
            Shopping.insert()
            pass
        else:
            f1 = open('E:/Python/Third/goods.txt','a',encoding='UTF-8')
            f1.write(no+'#'+name+'#'+kind+'#'+price+'#'+stock+'\n')
            f1.close()
            print('添加商品成功')
            pass
        pass

    @staticmethod
    def update():
        print('*******修改商品*******')
        print('请输入要修改的商品的编号')
        no = input("编号：")

        nos = []
        f = open('E:/Python/Third/goods.txt','r',encoding='UTF-8')
        for lines in f.readlines():
            lines=lines.replace('\n','').split('#')
            nos.append(lines[0])
            pass
        f.close()

        if no not in nos:
            print('此商品不存在，请重新输入')
            Shopping.delete()
            pass
        else:
            with open('E:/Python/Third/goods.txt','r',encoding='UTF-8') as f1:
                lines = f1.readlines()
                pass
            with open('E:/Python/Third/goods.txt','w',encoding='UTF-8') as f2:
                for line in lines:
                    line=line.replace('\n','').split('#')
                    if no in line[0]:
                        continue
                        pass
                    else:
                        f2.write(line[0]+'#'+line[1]+'#'+line[2]+'#'+line[3]+'#'+line[4]+'\n')
                        pass
                    pass
                pass
            f1.close()
            f2.close()
            pass

        print('请输入修改后的商品信息')
        
        no = input('编号：')
        name = input('名称：')
        kind = input('种类：')
        price = input('价格：')
        stock = input('库存：')

        f3 = open('E:/Python/Third/goods.txt','a',encoding='UTF-8')
        f3.write(no+'#'+name+'#'+kind+'#'+price+'#'+stock+'\n')
        f3.close()
        print('修改商品成功')
        pass
    
    @staticmethod
    def delete():
        print('*******删除商品页面*******')
        print('请输入要删除的商品的编号')
        no = input("编号：")

        nos = []
        f = open('E:/Python/Third/goods.txt','r',encoding='UTF-8')
        for lines in f.readlines():
            lines=lines.replace('\n','').split('#')
            nos.append(lines[0])
            pass
        f.close()

        if no not in nos:
            print('此商品不存在，请重新输入')
            Shopping.delete()
            pass
        else:
            with open('E:/Python/Third/goods.txt','r',encoding='UTF-8') as f1:
                lines = f1.readlines()
                pass
            with open('E:/Python/Third/goods.txt','w',encoding='UTF-8') as f2:
                for line in lines:
                    line=line.replace('\n','').split('#')
                    if no in line[0]:
                        continue
                        pass
                    else:
                        f2.write(line[0]+'#'+line[1]+'#'+line[2]+'#'+line[3]+'#'+line[4]+'\n')
                        pass
                    pass
                pass
            f1.close()
            f2.close()
            pass
        pass

    @staticmethod
    def shop():
        print('*******购买商品页面*******')
        print('请输入要购买的商品的编号和数量')
        try:
            no = input("编号：")
            num = int(input('数量：'))
            pass
        except ValueError:
            print("请输入数字")
            pass
        
        nos = []
        f = open('E:/Python/Third/goods.txt','r',encoding='UTF-8')
        for lines in f.readlines():
            lines=lines.replace('\n','').split('#')
            nos.append(lines[0])
            pass
        f.close()

        if no not in nos:
            print('此商品不存在，请重新输入')
            Shopping.shop()
            pass
        else:
            f1 = open('E:/Python/Third/goods.txt','r',encoding='UTF-8')
            lines = f1.readlines()
            f2 = open('E:/Python/Third/goods.txt','w',encoding='UTF-8')
            for line in lines:
                line = line.replace('\n','').split('#')
                if no in line[0]:
                    if num <= int(line[4]):
                        allprice = int(line[3])*num
                        f2.write(line[0]+'#'+line[1]+'#'+line[2]+'#'+line[3]+'#'+str(int(line[4])-num)+'\n')
                        print('购买商品价格为',allprice)
                        pass
                    else:
                        print('库存不足')
                        f2.write(line[0]+'#'+line[1]+'#'+line[2]+'#'+line[3]+'#'+line[4]+'\n')
                        f1.close()
                        f2.close()
                        Shopping.shop()
                        pass
                    pass
                else:
                    f2.write(line[0]+'#'+line[1]+'#'+line[2]+'#'+line[3]+'#'+line[4]+'\n')
                    pass
                pass
            f1.close()
            f2.close()
            
            condition = input('是否继续购买 Y/N：')
            if condition == 'Y':
                Shopping.shop()
                pass
            pass
        pass

    @staticmethod
    def exit():
        sys.exit(0)
        pass
    pass


while True:
    print('*******欢迎光临教育超市*******')
    print('1、登陆 2、注册 3、退出')
    try:
        opt1 = int(input('请输入选项：'))
        pass
    except ValueError:
        print("请输入数字")
        pass
    
    if opt1 == 1:
        Shopping.login()
        pass
    elif opt1 == 2:
        Shopping.register()
        pass
    elif opt1 == 3:
        Shopping.exit()
        pass
    else:
        print('输入有误，请重新输入')
        pass
    while True:
        print('*******购物页面*******')
        print('1、查看所有商品 2、根据商品种类查看商品 3、添加商品 4、修改商品 5、删除商品 6、购买商品 7、退出')
        try:
            opt2 = int(input('请输入选项：'))
            pass
        except ValueError:
            print("请输入数字")
            pass
        if opt2 == 1:
            Shopping.showAll()
            pass
        elif opt2 == 2:
            Shopping.showByKind()
            pass
        elif opt2 == 3:
            Shopping.insert()
            pass
        elif opt2 == 4:
            Shopping.update()
            pass
        elif opt2 == 5:
            Shopping.delete()
            pass
        elif opt2 == 6:
            Shopping.shop()
            pass
        elif opt2 == 7:
            break
            pass
        else:
            print('输入有误，请重新输入')
            pass
        pass
    pass

