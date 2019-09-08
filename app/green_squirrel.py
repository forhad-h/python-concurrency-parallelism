import time
from gevent.pool import Pool
from gevent import monkey

from utils import check_website
from websites import WEBSITE_LIST

NUM_WORKERS = 4

# Monky-Patcch socket module for HTTP requests
monkey.patch_socket()

start_time = time.time()

pool = Pool(NUM_WORKERS)

for address in WEBSITE_LIST:
    pool.spawn(check_website, address)

pool.join()

end_time = time.time()

print("Time for GreenSquirrel: %ssecs" % (end_time - start_time))
