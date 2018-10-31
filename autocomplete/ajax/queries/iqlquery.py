#!/usr/bin/python
import idol.aci as aci
maxresults = 3

def query(querytext=''):

  # add "IQL"
  # idol server parameters
  iql_action = "query&text=*"+querytext+"*&databaseMatch=IQLRules&maxresults="+str(maxresults)+"&print=all"
  autnresponse = aci.action(iql_action)
  # iterate over <autn:hit>
  iql = []
  for hit in autnresponse.findall("./responsedata/{http://schemas.autonomy.com/aci/}hit"):
    url_href = hit.find("{http://schemas.autonomy.com/aci/}content/DOCUMENT/DOCREF0").text
    title = hit.find("{http://schemas.autonomy.com/aci/}content/DOCUMENT/DRETITLE0").text
    iql.append('<a href="'+url_href+'">'+title+'</a>')

  # truncate the list to maxresults
  rhs = []
  i = 0
  j = len(iql)
  while i<j and i<maxresults:
    rhs.append(iql[i])
    i = i +1

  # prepare results
  if len(rhs):
    results = ['<hr/><strong>ABC/IQL</strong>'] + rhs
  else:
    results = []
  
  return results
