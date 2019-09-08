import time
from threading import Thread
from multiprocessing import Process

from tasks import only_sleep

NUM_WORKERS = 4


def run_serially():
    # run tasks serially
    start_time = time.time()

    for _ in range(NUM_WORKERS):
        only_sleep()

    end_time = time.time()

    print("Serial time=", end_time - start_time)


def run_threads():
    # Run tasks using threads
    start_time = time.time()

    threads = [Thread(target=only_sleep) for _ in range(NUM_WORKERS)]
    [thread.start() for thread in threads]
    [thread.join() for thread in threads]

    end_time = time.time()

    print("Threads time=", end_time - start_time)


def run_processes():
    # Run tasks using processes
    start_time = time.time()

    processes = [Process(
        target=only_sleep) for _ in range(NUM_WORKERS)]
    [process.start() for process in processes]
    [process.join() for process in processes]

    end_time = time.time()

    print("Parallel time=", end_time - start_time)
