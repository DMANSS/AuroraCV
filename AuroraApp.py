import cgi
import html
import FrameVideo

cam = FrameVideo.Videocam()

form = cgi.FieldStorage()
text1 = form.getfirst("TEXT_1", "не задано")
text2 = form.getfirst("TEXT_2", "не задано")
text1 = html.escape(text1)
text2 = html.escape(text2)


print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="utf-8">
            <title>AuroraClient</title>
        </head>
        <body>""")

print("<h1>Client</h1>")
print("<p>Timeline: {}</p>".format(text1))
print("<p>Object: {}</p>".format(text2))
print("<img src='{}'>", img)
print('<video width="320" height="240" poster="/images/w3html5.gif" controls>')
print('<source src="movie.mp4" type="video/mp4">')
print('<source src="movie.ogg" type="video/ogg">')
print("Your browser does not support the video tag.")
print("</video>")
print("""</body>
        </html>""")
