import http.server
import socketserver

form = '''<!DOCTYPE html>
<title>Message Board</title>
<form method="POST" action="http://localhost:8000/">
<textarea name="message"></textarea>
<br>
<button type="submit">Post it!</button>
</form>
'''

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(form.encode()) 

    def do_POST(self):
        length = int(self.headers.get('Content-length', 0))
        data = self.rfile.read(length).decode()
        message = parse_qs(data)["message"][0]

        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        self.wfile.write(message.encode())

handler_object = MyHttpRequestHandler

PORT = 8080
my_server = socketserver.TCPServer(("", PORT), handler_object)

# Star the server
my_server.serve_forever()
