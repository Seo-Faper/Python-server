import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        elif self.path == '/write':
            self.path = 'write.html'
        elif self.path =='/broadcast':
            self.path = 'broadcast.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        print(self)

        return http.server.SimpleHTTPRequestHandler.do_POST(self)
# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8000
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()
