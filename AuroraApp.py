from http.server import HTTPServer, CGIHTTPRequestHandler
import SSV
import faceDet
server_address = ("", 8000)
httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
httpd.serve_forever()

cam = SSV.Videocam()
cam1 = faceDet()
cam.detect()