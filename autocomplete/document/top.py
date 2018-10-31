#!/usr/bin/python
import document.head.top as head
import document.body.top as body

print "Content-Type: text/html"
print
print """\
<html>"""

head.render()
body.render()

print """\
</html>
"""
