import socket
import time
import os 

DNS_QUERY = os.getenv('DNS_QUERY', 'www.google.com')
          
def resolve():
    i=0
    start_time = 0
    try:
        for i in range(10):
            i = i + 1
            start_time = time.time()
            socket.getaddrinfo( DNS_QUERY, 443, 0, socket.SOCK_STREAM)
    except Exception, e:
        print "failure: %s (start time: %s, exception time: %s)" % (e,
                str(start_time), str(time.time()))

while True: 
   resolve()
   time.sleep(5)
