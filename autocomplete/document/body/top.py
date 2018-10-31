#!/usr/bin/python
from document.body import params
from document.body import banner
from document.body import queryform
from document.body import results

def render():
  querytext = params.querytext
  print """\
  <body><div align = "left">
  """
  banner.render()
  queryform.render(querytext)
  results.render(querytext)
  print "</div></body>"
