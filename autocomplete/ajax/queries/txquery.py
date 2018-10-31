#!/usr/bin/python
import idol.aci as aci
maxresults=3
def query(querytext=''):

  # idol server parameters
  tx_action = "termexpand&text="+querytext+"&databaseMatch=&expansion=wild&maxterms="+str(maxresults)+"&mindococcs=10&stemming=false&type=dococcs&systemquery=true"
  autnresponse = aci.action(tx_action)

  # iterate over <autn:term>
  tx = []
  for term in autnresponse.findall("./responsedata/{http://schemas.autonomy.com/aci/}term"):
    tx.append(term.text)

  # truncate the list to maxresults
  rhs = []
  i = 0
  j = len(tx)
  while i<j and i<maxresults:
    rhs.append(tx[i])
    i = i +1

  # prepare results
  if len(rhs):
    results = ['<hr/><strong>Suggested Terms</strong>'] + rhs
  else:
    results = []

  return results
