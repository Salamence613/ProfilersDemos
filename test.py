import time
import cProfile

def func1():
    time.sleep(1)

def main():
    for i in range(10):
        func1()

cProfile.run("main()", filename="test.prof", sort=-1)