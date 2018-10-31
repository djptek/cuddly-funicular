#!/usr/bin/python
from document.head import meta
from document.head import styles
from document.head import scripts

def render():
  print """<head>
  """
  meta.render()
  styles.render()
  scripts.render()
  print """</head>
  """
