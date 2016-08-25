# -*- coding: utf-8 -*-
# Author Keijo Korte / 24.08.2016

class ParsedVuln:
  title = ""
  link = ""
  desc = ""
  prio = "MED"
  
  

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
