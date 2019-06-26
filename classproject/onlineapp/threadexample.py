import time
import threading

counter=0

def update():
    global counter
    name=threading.current_thread().name
    for i in range(10):
        counter+=1
        print(name,"i value ",i,"counter value ",counter)
        time.sleep(0.1)

def activity(tag):
    for i in range(5):
        thread_id = threading.current_thread().ident
        print("hello from",tag,"i = ",i,"thread_id = ",thread_id)
        time.sleep(i)


def worker2():
    print("worker2 = ",threading.current_thread().ident)
    activity("worker2")

def worker1():
    print("worker1 = ", threading.current_thread().ident)
    activity("worker1")

def process1():
    global counter
    while True:
        counter+=1

def process2():
    global counter
    while True:
        counter+=1

def output():
    while True:
        print("countet value is = ",counter)

def main():
    threads=[]
    for i in range(10):
        thread=threading.Thread(target=process1)
        threads.append(thread)
        thread.start()

    thread3 = threading.Thread(target=output)
    thread3.start()
    thread3.join()

if __name__ == '__main__':
    main()