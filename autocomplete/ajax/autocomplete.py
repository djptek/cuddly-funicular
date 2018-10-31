#!/usr/bin/python
import cgi
import sys

# add sys path to leverage idol package
sys.path.append("/usr/lib/cgi-bin/autocomplete")

form = cgi.FieldStorage() # instantiate only once!
querytext = form.getfirst('term', '')
querytext = cgi.escape(querytext)

from queries import acqueries
print '''
%s''' % acqueries.query(querytext)


