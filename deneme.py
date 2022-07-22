import time


def countdown(t):
    
    while t:
        t=5
        mins, secs = divmod(t,60)
        timer = '{02d}:{:02d}'.format(mins,secs)
        t -= 1
        

