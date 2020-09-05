# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 15:08:15 2020

@author: shata
"""
#Drink Water Reminder application in Python
import time
from plyer import notification
if __name__=="__main__":
    while True:
        
        notification.notify(
            title = "Please Drink Water now!!",
            message = "Adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon = "C:\Python Projects\water reminder\waterglass.ico",
            timeout=10
        )        
        time.sleep(60*60)
