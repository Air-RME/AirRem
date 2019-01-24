import time
import redis
import importlib
# import transmitter as ir
# import signal
# import sys
# import os

class Receiver:
    # OPTION
    SURVEILLANCE_INTERVAL = 1
    REDIS_LISTNAME = 'order'
    runCodeQueue = redis.Redis(host='localhost', port=6379)

    @classmethod
    def run(self):
        try:
            while True:
                time.sleep(self.SURVEILLANCE_INTERVAL)
                if self.runCodeQueue.llen(self.REDIS_LISTNAME) != 0:
                    runKey = self.runCodeQueue.lpop(self.REDIS_LISTNAME).decode('utf-8')
                    ir.transmission(runKey)

        except KeyboardInterrupt:
            print("error receiver")
            pass