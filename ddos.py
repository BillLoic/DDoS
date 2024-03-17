import http.client as http
import sys

host = sys.argv[1]

while True:
    print("Sending request to %s......" % host)
    request_pool = http.HTTPSConnection(host=host)
    request_pool.request(method="GET", url = "/")
    
