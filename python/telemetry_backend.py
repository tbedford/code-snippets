# Python 3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
from urllib.parse import parse_qs
from pprint import pprint

import time
import json

hostName = "localhost"
hostPort = 9000

OK = 200

# Webhook params
# {'keyword': ['TEST'],
# 'message-timestamp': ['2018-04-16 11:19:22'],
# 'messageId': ['0C000000A7438C74'],
# 'msisdn': ['447931550511'],
# 'text': ['Test yo!'],
# 'to': ['447418340545'],
# 'type': ['text']}

class MyServer(BaseHTTPRequestHandler):
    
    def do_GET(self):

        self.send_response(OK)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        if self.path.startswith('/webhooks/inbound-sms'):
        
            result = urlparse(self.path)
            params = parse_qs(result.query)
            data = params['text'][0]

            print ("Telemetry data is: %s" % data)

            
# Run server        
myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))
        
try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass
    
myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

