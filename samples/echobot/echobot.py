import http.server

class BotHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        print("POST: ", self.path)

        request_headers = self.headers
        content_length = self.headers['content-length']
        length = int(content_length[0]) if content_length else 0
        
        print(request_headers)
        print(self.rfile.read(length))
        self.send_response(200)

if __name__ == '__main__':
    PORT = 3978
    httpd = http.server.HTTPServer(("", PORT), BotHandler)

    print (httpd.server_name, " listening to ", httpd.server_port)
    httpd.serve_forever()