# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 11:18:23 2019

@author: Shakir Hussain
"""

import threading
import time

def sleeper(n,name):
        time.sleep(1)
        print('I am {} and going to sleep for {} seconds now!\n'.format(name,n))
        time.sleep(n)
        print('{} woken up!\n'.format(name))

#Spawning Threads  
thread_list=[]
start=time.time()
for i in range(5):
    t=threading.Thread(target=sleeper,name='Thread{}'.format(i),args=(5,'Thread{}'.format(i)))
    thread_list.append(t)
    t.start() #Calling Thread Function
    print('Thread {} has started'.format(t.name))
    #t.join() #join call is helpful to complete thread function execution by making Main Program waiting. Try uncomment this line and observe change in behavior
for t in thread_list:
    t.join()
    
end=time.time()
#While Thread Function Executes Main Thread continues its execution
print('We are in Main Program and threads execution took {} Seconds'.format(end-start))