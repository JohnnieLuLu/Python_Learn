import time,threading

__author__ = 'Kevin'

balance = 0
lock = threading.Lock()

def changeIn(n):
	global balance
	balance = balance + n

def changeOut(m):
	global balance
	balance = balance - m
	
def runIn(n):
	lock.acquire()
	changeIn(n)
	print('存款线程%s正在运行,存入金额为%s' %(threading.current_thread().name,n))
	lock.release()

def runOut(m):
	lock.acquire()
	changeOut(m)
	print('取款线程%s正在运行,取出金额为%s' %(threading.current_thread().name,m))
	lock.release()
	
t1 = threading.Thread(target = runIn, name = 'Store',args = (20,))
t2 = threading.Thread(target = runOut, name = 'outPut',args = (10,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
