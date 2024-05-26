import time
import cProfile

def longSleep():
    time.sleep(1)

def shortSleep():
    time.sleep(0.1)

def main():
    for _ in range(10):
        shortSleep()
    
    for _ in range(3):
        longSleep()

cProfile.run("main()", filename=None, sort=-1)