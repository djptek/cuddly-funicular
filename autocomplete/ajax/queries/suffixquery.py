#!/usr/bin/python
import idol.aci as aci
import re
import string

maxresults = 5

def query(querytext=''):

  # add "suffix" query
  # idol server parameters
  suffixes_action = "query&text="+querytext+"&matchallterms=true&databaseMatch=&systemquery=true&maxresults=10&print=none&printfields=DRECONTENT"
  getsuffix = re.compile('('+querytext+'[ \w][^ ,.%*")(]*) ')

  autnresponse = aci.action(suffixes_action)
  # iterate over <autn:hit>
  suffixes = []
  for hit in autnresponse.findall("./responsedata/{http://schemas.autonomy.com/aci/}hit"):
    drecontent = hit.find("{http://schemas.autonomy.com/aci/}content/DOCUMENT/DRECONTENT").text
    for suffix in getsuffix.findall(drecontent):
      if suffix not in suffixes: 
        suffixes.append(suffix)

  # truncate the list to maxresults
  rhs = []
  i = 0
  j = len(suffixes)
  while i<j and i<maxresults:
    rhs.append(suffixes[i])
    i = i +1

  # prepare results
  if len(rhs):
    results = ['<hr/><strong>Phrase Match</strong>'] + rhs
  else:
    results = []
  
  return results
