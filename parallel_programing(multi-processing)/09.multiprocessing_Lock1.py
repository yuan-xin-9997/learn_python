# -*- coding: utf-8 -*-

# File Name： 09.multiprocessing_Lock1
# Description :
# Author : yuan.xin
# create_date： 2023/9/14
# Change Activity:
"""
Lock（互斥锁）
Lock锁的作用是当多个进程需要访问共享资源的时候，避免访问的冲突。
加锁保证了多个进程修改同一块数据时，同一时间只能有一个修改，即串行的修改，牺牲了速度但保证了数据安全。Lock包含两种状态——锁定和非锁定，以及两个基本的方法。
"""