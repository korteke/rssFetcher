# -*- coding: utf-8 -*-
# Author Keijo Korte / 25.08.2016

import feedparser, time, os
import cPickle as pickle
from ParsedVuln import ParsedVuln
import HelperTools
from jira import JIRA

# Variables
FEEDS = [ "https://www.viestintavirasto.fi/rss/haavoittuvuudet.xml"]
MOD_FILE = "modified.p"
JIRA_URL = "https://SERVER"
JIRA_OPTIONS = { 'server': JIRA_URL }
JIRA_USER = "USER"
JIRA_PASSWD = "PASSWORD"
JIRA_PROJECT = 123456

def getFeed(url,modi,seq):
  ''' Get feed from url '''
  f = feedparser.parse(url, modified=modi)
  if f.status == 200 and (f.version == 'rss20' or f.version == 'rss10'):
    vuln = ParsedVuln(f.entries[0].title,f.entries[0].link,f.entries[0].description)
    setModi(f.modified,seq)
    return vuln
  if f.status == 304:
    return None
  else:
    print "Error. Can't fetch feed from " + url
    HelperTools.notifyAdmins(f.status)
    return None

def getModi(seq):
    ''' Get modified timestamp from pickled file '''
    try:
      if not os.path.exists(MOD_FILE+seq):
        fakeTime = "Tue, 05 Oct 1982 06:36:06 GMT"
        with open(MOD_FILE+seq, 'wb') as f:
          pickle.dump(fakeTime, f)
          f.close()
        with open(MOD_FILE+seq, 'rb') as f:
          modi =  pickle.load(f)
          f.close()
          return modi
      else:
        with open(MOD_FILE+seq, 'rb') as f:
          modi = pickle.load(f)
          f.close()
          return modi
    except IOError, e:
      print "Error: " + str(e)
      return None

def setModi(modi,seq):
    ''' Add modified timestamp to the file '''
    with open(MOD_FILE+seq, 'wb') as f:
      pickle.dump(modi, f)
      f.close()

def createJiraTicket(vuln):
    ''' Create JIRA ticket '''
    issue_dict = {
      'project': {'name': JIRA_PROJECT},
      'summary': vuln.getTitle(),
      'description': vuln.getDesc()+"\n\n"+vuln.getLink(),
      'priority': {'name': vuln.getPrio()},
      'issuetype': {'name': vuln.getIssueType()},
      'components': [{'name': vuln.getComponent()}],
      'customfield_10007': {'value': vuln.getSeverity()}
    }

    try:
      jira = JIRA(JIRA_OPTIONS, basic_auth=(JIRA_USER, JIRA_PASSWD))
      issue = jira.create_issue(project="PLATTA", summary=vuln.getTitle(), description=vuln.getDesc()+"\n\n"+vuln.getLink(), issuetype={'name': 'Defect'}, components=[{'name': vuln.getComponent()}], customfield_10001={'value': vuln.getPhaseId()})
      #issue = jira.create_issue(fields=issue_dict)
      print "Creating JIRA ticket"
      print "Ticket " + str(issue) + " created\n"
    except Exception as e:
      print "Failed to create a ticket"
      print e
      HelperTools.notifyAdmins(e)

def main():
  ''' Main program. Loop's through FEEDS array '''
  j = 1
  for i in FEEDS:
    feed = getFeed(i,getModi(str(j)),str(j))
    j = j+1
    if feed is None:
      pass
    else:
      print "New vulnerabilities"
      print feed.getTitle() + " - " + feed.getLink()
      createJiraTicket(feed)

if __name__ == "__main__": main()
