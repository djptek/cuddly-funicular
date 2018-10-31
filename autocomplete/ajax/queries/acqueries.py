#!/usr/bin/python
import json
from queries import iqlquery
from queries import spellquery
from queries import recentquery
# dedup merges the relusts of suffix & tx
from queries import dedup

def query(querytext=''):

  # package as JSON and return
  return json.JSONEncoder().encode(\
    dedup.query(querytext)+
    spellquery.query(querytext)+
    iqlquery.query(querytext)+
    recentquery.query(querytext))

