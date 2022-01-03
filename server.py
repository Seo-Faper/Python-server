import http.server
import socketserver
from urllib import parse


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
        length = int(self.headers.get('Content-length', 0))
        data = self.rfile.read(length).decode()
        if self.path== '/loginAction':
            id = parse.parse_qs(data)["userID"][0]
            pw = parse.parse_qs(data)["userPassword"][0]


        print(f"id :{id}")
        print(f"pw :{pw}")


        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        self.wfile.write(message.encode())

# Create an object of the above class
handler_object = MyHttpRequestHandler

PORT = 8080
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()
