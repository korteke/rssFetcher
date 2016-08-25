# -*- coding: utf-8 -*-
# Author Keijo Korte / 25.08.2016

class ParsedVuln:
  title = ""
  link = ""
  desc = ""
  prio = "Medium"
  severity = "Medium"
  component = "vuln_mgmt"
  issueType = "Task"
  
  def __init__(self, title, link, desc):
    self.title = title
    self.link = link
    self.desc = desc

  def getTitle(self):
    return  self.title

  def getLink(self):
    return self.link

  def getDesc(self):
    return self.desc

  def getPrio(self):
    return self.prio

  def getSeverity(self):
    return self.severity

  def getComponent(self):
    return self.component

  def getIssueType(self):
    return self.issueType
