#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    ip_parts = [random.randint(1, 255) for _ in range(4)]
    ip = ".".join(map(str, ip_parts))
    status = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    size = random.randint(1, 1024)
    log_line = "{} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        ip,
        datetime.datetime.now(),
        status,
        size,
    )
    sys.stdout.write(log_line)
    sys.stdout.flush()
