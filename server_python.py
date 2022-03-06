from http.server import BaseHTTPRequestHandler, HTTPServer
from calc_rent import calculate
import time
import json

PORT = 8000

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        message = "Hello, World! Here is a GET response"
        print(message)
        content_len = int(self.headers.get('content_len',0))
        body = self.rfile.read(content_len)
        print(body)
        self.wfile.write(bytes(message, "utf8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','application/json')
        self.end_headers()
        message = "POST request received loading data\n"
        time.sleep(2)
        content_length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(content_length)
        self.write_response_and_calc(body)


    def write_response_and_calc(self, content):
        # self.wfile.write(content)
        print("data received from post request : \n")
        time.sleep(2)
        res = calculate(content)
        print("send result\n")
        time.sleep(2)
        print("calc result is :" + str(res))
        res = json.dumps(res)
        print(res)       
        self.wfile.write(b"res")


with HTTPServer(('', PORT), handler) as server:
    print("server listen on http://localhost:"+str(PORT))
    server.serve_forever()
