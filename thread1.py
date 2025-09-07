import threading


def print_num():
    for i in range(1,5):
        print(i)


t1 = threading.Thread(target=print_num)
t2 = threading.Thread(target=print_num)

t1.start()
t2.start()

t1.join()
t2.join()