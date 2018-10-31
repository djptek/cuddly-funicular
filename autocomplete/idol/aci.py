#!/usr/bin/python
import httplib
import xml.etree.ElementTree as etree
import config

def action(action_param_value_pairs):
  # build connection to IDOL
  conn = httplib.HTTPConnection(config.server+":"+str(config.aci_port))
  conn.request("GET", "/action="+action_param_value_pairs)
  r1 = conn.getresponse()
  # read the xml as a string
  xml = r1.read()
  conn.close()

  # return autnresponse
  return etree.fromstring(xml)
