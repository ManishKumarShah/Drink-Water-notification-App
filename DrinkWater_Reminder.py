from email import message
import time

from matplotlib.pyplot import title 
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title= "***Please Drink Water Now!",
            message='''Drinking water can prevent dehydration, 
            a condition that can cause unclear thinking, 
            result in mood change, cause your body to overheat, and 
            lead to constipation and kidney stones>''',
            app_icon="/home/manishkumarshah/Manish Python Program/Practice Program/drink-water.png",
            timeout = 10 #notificaion duration to appear on screen

        )
        time.sleep(60*60)#every 1 hour notification will run


        