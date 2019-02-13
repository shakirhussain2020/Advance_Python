# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 10:24:39 2019

@author: Shakir Hussain
"""

import threading
import time

def sleeper(n,name):
        time.sleep(3)
        print('I am {} and going to sleep for {} seconds now!'.format(name,n))
        time.sleep(n)
        print('{} woken up!'.format(name))

#Spawning Threads        
t=threading.Thread(target=sleeper,name='Thread1',args=(5,'Thread1'))
t.start() #Calling Thread Function
#t.join() #join call is helpful to complete thread function execution by making Main Program waiting. Try uncomment this line and observe change in behavior

#While Thread Function Executes Main Thread continues its execution
time.sleep(4)
print('We are in Main Program')
time.sleep(2)
print('We are still in Main Program')