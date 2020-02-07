import os
import http.server as s
from urllib.parse import urlparse
from urllib.parse import parse_qs

class HttpHandler(s.BaseHTTPRequestHandler):
    def do_GET(self):
        self.exec()

    def do_POST(self):
        self.exec()

    def exec(self):
        parsed = urlparse(self.path)
        params = parse_qs(parsed.query)
        content_length  = int(self.headers.get("content-length"))
        req_body = self.rfile.read(content_length).decode("utf-8")

        print("---REQUEST---")
        print(str(self.headers) + "\n")

        body  = "method: " + str(self.command) + "\n"
        body += "params: " + str(params) + "\n"
        body += "body  : " + req_body + "\n"

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.send_header('Content-length', len(body.encode()))
        self.end_headers()
        self.wfile.write(body.encode())

host = '0.0.0.0'
port = 8000
httpd = s.HTTPServer((host, port), HttpHandler)
print('Server started. port:%s' % port)
httpd.serve_forever()
