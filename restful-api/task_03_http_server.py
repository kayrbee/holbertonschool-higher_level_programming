#!/usr/bin/python3
import http.server
import socketserver
import json


PORT = 8000
data = {"name": "John", "age": 30, "city": "New York"}
info = {"version": "1.0", "description": "A simple API built with http.server"}

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")  # NB: must be binary string
        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            json_data = json.dumps(data)
            self.wfile.write(json_data.encode("utf-8"))
        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            json_info = json.dumps(info)
            self.wfile.write(json_info.encode("utf-8"))
        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"200 OK")            
        else:
            self.send_error(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Page Not Found")

# Start the server
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port ", PORT)
    httpd.serve_forever()
