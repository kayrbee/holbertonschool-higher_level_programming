#!/usr/bin/python3
import http.server
import socketserver


PORT = 8000

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, world!")  # NB: must be binary string

# Start the server
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print("serving at port ", PORT)
    httpd.serve_forever()
