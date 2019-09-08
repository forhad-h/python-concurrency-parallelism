from os import getpid
from time import sleep
from threading import current_thread
from multiprocessing import current_process


def only_sleep():
    # only sleep task
    print("PID: %s, Process Name: %s, Thread Name: %s" % (
        getpid(),
        current_process().name,
        current_thread().name
    ))
    sleep(1)  # wait for 1 sec


def crunch_numbers():
    # some calculation task
    print("PID: %s, Process Name: %s, Tread Name: %s" % (
        getpid(),
        current_process().name,
        current_thread().name
    ))
    x = 0
    while x < 10000000:
        x += 1
