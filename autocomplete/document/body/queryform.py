#!/usr/bin/python
def render(querytext):
  print """
<table width="800px">
  <tr>
    <td align="left">
      <form id="queryForm" method="get" action="default.py">
        <input id="queryField" type="text" name="querytext" size="64" value="%s"/>
        <input type="submit" name="submitbutton" value="OK"/>
      </form>
  </tr>
</table>
""" % querytext
