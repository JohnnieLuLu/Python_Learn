class User(object):
    def __init__(self,username,pwd):
        self.username = username
        self.pwd = pwd
        pass
    def __str__(self):
        ss = "用户名：{0},密码：{1}".format(self.username,self.pwd)
        return ss
        pass
    pass