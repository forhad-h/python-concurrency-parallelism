import time
import socket
import multiprocessing

from utils import check_website
from websites import WEBSITE_LIST

NUM_WORKERS = 4

star_time = time.time()

with multiprocessing.Pool(processes=NUM_WORKERS) as pool:
    results = pool.map_async(check_website, WEBSITE_LIST)
    results.wait()

end_time = time.time()

print("Time for MultiProcessingSquirrel: %ssecs" % (end_time - star_time))
