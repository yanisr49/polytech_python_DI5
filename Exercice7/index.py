#!/usr/bin/python3
import http.server
import cgi
import socketserver

PORT = 8888

form = cgi.FieldStorage()

print("Content-type: text/html; charset=utf-8\n")

name = form.getvalue("name")
password = form.getvalue("password")

if name == "paul" and password == "retail":
    httpd = http.HTTPServer(('bingo.py', 8888), http.SimpleHTTPRequestHandler) # marche pas
    httpd.serve_forever()

html = """<!DOCTYPE html>
<head>
 <title>Mon programme</title>
</head>
<body>
 <form action="/index.py" method="post">
 <input type="text" name="name" value="paul" />
 <input type="password" name="password" value="retail" />
 <input type="submit" name="send" value="Envoyer information au serveur">
 </form>
</body>
</html>
"""
print(html)