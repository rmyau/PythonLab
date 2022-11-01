from http.server import HTTPServer
from http.server import CGIHTTPRequestHandler
address = ('localhost', 8000)
serv = HTTPServer(address, CGIHTTPRequestHandler)
serv.serve_forever()
