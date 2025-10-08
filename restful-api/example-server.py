import http.server
import socketserver


PORT = 8080
Handler = http.server.SimpleHTTPRequestHandler
# SimpleHTTPRequestHandler is a simple HTTP request handler that serves
# files from the current directory and any of its subdirectories.
# It will look for the index file first


with socketserver.TCPServer(("", PORT), Handler) as httpd:
    # socketserver.TCPServer describes a server that uses the TCP protocol
    # to send and receive messages
    # It takes a tuple of (address, port) to specify where to listen
    # and a handler to specify what to do
    print("serving at port ", PORT)
    httpd.serve_forever()  # Start server and continue indefinitely

# To start the server:
# python3 example-server.py

# To see it running:
# http://localhost:8080/