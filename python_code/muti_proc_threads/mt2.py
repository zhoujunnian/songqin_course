# coding=utf8
import threading
from time import sleep

# 存储支付宝账号余额
zhifubao = {
    'jcy'     : 2000,
    'liming'  : 5000,
    'wangan'  : 15000,
    'zhaolei' : 6005000,
}

# 线程1 ： 滴滴打车处理，参数是用户账户和扣款金额
def thread1_didi_pay(account,amount):
    print('* t1: get balance from bank')
    balance = zhifubao[account]

    # 下面的sleep(2) 表示一些处理过程需要花上2秒钟
    print('* t1: do something(like discount lookup) for 2 seconds')
    sleep(2)

    print('* t1: deduct')
    zhifubao[account] = balance - amount

# 线程2 ： 余额宝处理，参数是用户账户和当前利息
def thread2_yuebao_interest(account,amount):
    print('$ t2: get balance from bank')
    balance = zhifubao[account]

    # 下面的sleep(1) 表示一些处理过程需要花上1秒钟
    print('$ t2: do something2.... for 1 seconds')
    sleep(1)

    print('$ t2: add')
    zhifubao[account] = balance + amount



t1 = threading.Thread(target=thread1_didi_pay,    args=('jcy',10))
t2 = threading.Thread(target=thread2_yuebao_interest, args=('jcy',10))
t1.start()
t2.start()
t1.join()
t2.join()
print('finally, jcy balance is %s' % zhifubao['jcy'])
