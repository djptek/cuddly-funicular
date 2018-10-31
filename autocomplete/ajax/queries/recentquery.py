#!/usr/bin/python
import re
import string
import idol.service as service

systemquery=re.compile('systemquery=true',re.IGNORECASE)
nomatch=re.compile('Returning 0 matches')
hastext=re.compile('&text=',re.IGNORECASE)
gettext=re.compile('text=(\w*)',re.IGNORECASE)
maxresults=3

def query(querytext):

  # idol server parameters
  recent_action = "GetLogStream&Name=%2Fopt%2FAutonomy%2FIDOLServer10%2FIDOL%2Flogs%2Fcontent_query.log&FromDisk=true&Tail=500"
  raw = service.action(recent_action)

  # iterate over <autn:term>
  matches = []

  #hasquerytext=re.compile(querytext,re.IGNORECASE)
  queryterms = string.split(querytext.lower(),' ')

  for line in raw.split('action'):
    if not systemquery.search(line)\
      and not nomatch.search(line)\
      and hastext.search(line):
        textparam = string.split(gettext.findall(line)[0].lower(),' ')
        intersect = set(textparam) & set(queryterms)
        if len(intersect)\
          and list(intersect)[0] not in matches:
          matches.append(list(intersect)[0])

  # reverse the list, taking maxresults
  rhs = []
  i = len(matches)
  j = i - maxresults
  while i and i>j:
    i = i -1
    rhs.append(matches[i])

  # prepare results
  if len(rhs):
    results = ['<hr/><strong>Recent Searches</strong>'] + rhs
  else:
    results = []
  
  return results
