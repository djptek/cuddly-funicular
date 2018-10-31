#!/usr/bin/python
import idol.aci as aci
maxresults = 3

def query(querytext=''):

  # idol server parameters
  spell_action = "query&text="+querytext+"&spellcheck=true&print=nospell&singleresult=true&systemquery=true"
  autnresponse = aci.action(spell_action)

  # iterate over <autn:term>
  spell = []
  for term in autnresponse.findall("./responsedata/{http://schemas.autonomy.com/aci/}spellingquery"):
    spell.append(term.text)

  # truncate the list to maxresults
  rhs = []
  i = 0
  j = len(spell)
  while i<j and i<maxresults:
    rhs.append(spell[i])
    i = i +1

  # prepare results
  if len(rhs):
    results = ['<hr/><strong>Spellcheck</strong>'] + rhs
  else:
    results = []

  return results
