#!/usr/bin/python3
import http.server
import socketserver
import json


PORT = 8000
data = {"name": "John", "age": 30, "city": "New York"}

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
            json_string = json.dumps(data)
            self.wfile.write(json_string.encode("utf-8"))  # NB: must be binary string
        else:
            self.send_error(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Page Not Found")  # NB: must be binary string

# Start the server
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port ", PORT)
    httpd.serve_forever()
