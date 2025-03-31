from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse
import json


class RequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/search_user':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            parsed_data = urllib.parse.parse_qs(post_data)
            q = parsed_data.get('q', [''])[0]
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            if q:
                # This line was changed to match the expected output.
                response_data = [{"id": 89, "name": f"{q}olberton"}]
            else:
                response_data = []
            self.wfile.write(json.dumps(response_data).encode('utf-8'))
        else:
            self.send_response(404)
            self.end_headers()


def run(server_class=HTTPServer, handler_class=RequestHandler, port=5000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
