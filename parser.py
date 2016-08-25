# -*- coding: utf-8 -*-
# Author Keijo Korte / 24.08.2016

import feedparser, time, os
import cPickle as pickle
from ParsedVuln import ParsedVuln
from jira import JIRA

URL = "https://www.viestintavirasto.fi/rss/haavoittuvuudet.xml"
MOD_FILE = "modified.p"
JIRA_URL = "http://localhost:8080"
JIRA_OPTIONS = { 'server': JIRA_URL }
JIRA_USER = "api"
JIRA_PASSWD = "apina123!"
JIRA_PROJECT = 10000
JIRA_DEF_PRIO = "High"

def getFeed(url,modi):
  f = feedparser.parse(url, modified=modi)
  if f.status == 200:
    vuln = ParsedVuln(f.entries[0].title,f.entries[0].link,f.entries[0].description)
    setModi(f.modified)
    return vuln
  if f.status == 304:
    return None
  else:
    print "Perkele"

def getModi():
    try:
      if not os.path.exists(MOD_FILE):
        fakeTime = "Tue, 05 Oct 2016 06:36:06 GMT"
        with open(MOD_FILE, 'wb') as f:
          pickle.dump(fakeTime, f)
          f.close()
        with open(MOD_FILE, 'rb') as f:
          modi =  pickle.load(f)
          f.close()
          return modi
      else:
        with open(MOD_FILE, 'rb') as f:
          modi = pickle.load(f)
          f.close()
          return modi
    except IOError, e:
      print "Error: " + str(e)
      return None 

def setModi(modi):
    with open('modified.p', 'wb') as f:
      pickle.dump(modi, f)
      f.close()

def createJiraTicket(vuln):
    jira = JIRA(JIRA_OPTIONS, basic_auth=(JIRA_USER, JIRA_PASSWD))

    issue_dict = {
      'project': {'id': JIRA_PROJECT},
      'summary': vuln.getTitle(),
      'description': vuln.getDesc(),
      'priority': {'name': JIRA_DEF_PRIO},
      'issuetype': {'name': 'Task'},
    }
    issue = jira.create_issue(fields=issue_dict)
    print "Creating JIRA ticket: " + str(issue)

def main():
  feed = getFeed(URL,getModi())
  if feed is None:
    print "None"
  else:
    print "New vulnerabilities"
    print feed.getTitle() + " - " + feed.getLink()
    createJiraTicket(feed)
    
if __name__ == "__main__": main()
