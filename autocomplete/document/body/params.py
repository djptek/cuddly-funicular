#/usr/bin/python
import cgi
import string

form = cgi.FieldStorage() # instantiate only once!
querytext = string.replace(form.getfirst('querytext', ''),'&nbsp;&nbsp;','')
querytext = cgi.escape(querytext)

