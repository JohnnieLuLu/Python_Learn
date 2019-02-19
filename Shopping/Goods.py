class Goods(object):
    def __init__(self,no,name,kind,price,stock):
        self.no = no
        self.name = name
        self.kind = kind
        self.price = price
        self.stock = stock
        pass
    def __str__(self):
        ss = "编号：{0}，名称：{1}，种类：{2}，价格：{3}，库存：{4}".format(self.no,self.name,self.kind,self.price,self.stock)
        return ss
        pass
    pass