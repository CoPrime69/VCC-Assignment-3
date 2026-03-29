#! /bin/bash
sudo apt update
sudo apt install -y python3

cat > app.py <<EOF
from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Hello from GCP Auto-Scaled VM - Assignment 3rd")

server = HTTPServer(("0.0.0.0", 8000), Handler)
server.serve_forever()
EOF

python3 app.py