#!/usr/bin/python
import string
import txquery
import suffixquery

maxresults = 5

def query(querytext=''):

  dedup = []
  for sxtx in txquery.query(querytext) + suffixquery.query(querytext):  
    if "<hr/>" not in sxtx and\
      sxtx.lower() not in dedup:
      dedup.append(sxtx)

  # truncate the list to maxresults
  rhs = []
  i = 0
  j = len(dedup)
  while i<j and i<maxresults:
    rhs.append(dedup[i])
    i = i +1

  # prepare results
  if len(rhs):
    results = ['<hr/><strong>Phrase/Term Expand</strong>'] + rhs
  else:
    results = []
  
  return results
