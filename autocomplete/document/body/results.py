#!/usr/bin/python
import idol.aci as aci
import string

def render(querytext):
  print """\
<table width="800px" class="results">
  <tr>
    <td><h2>results for %s</h2></td>
  </tr>""" % querytext

  # idol server parameters
  query_action = "query&text="+querytext+"&databaseMatch=particulars+empresas&systemquery=false&maxresults=10&fieldtext=EXISTS{}:TITLE&summary=context&outputencoding=ASCII"
  autnresponse = aci.action(query_action)
  
  # iterator over <autn:hits>
  hits = autnresponse.findall("./responsedata/{http://schemas.autonomy.com/aci/}hit")
  
  # look for hits that have seats in use and print detail
  for hit in hits:
      ref = hit.find("{http://schemas.autonomy.com/aci/}reference").text
      lref = string.replace(ref,"/var/Webroot/DEMO/www","http://127.0.0.1")
      dref = string.replace(ref,"/var/Webroot/DEMO/www","http://")
      tit = hit.find("{http://schemas.autonomy.com/aci/}title").text
      #print "<tr><td><a href=\"+lref+"\">"+dref+"<a/><br/>"+tit+"<br/><br/></td></tr>"
      print "<tr><td><a href=\""+lref+"\">"+dref+"<a/><br/>"+tit.encode('utf-8')+"<br/><br/></td></tr>"
  print """\
</table>"""

