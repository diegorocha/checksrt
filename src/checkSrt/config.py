#!/usr/bin/env python
#-*- coding: UTF-8 -*-

from os.path import abspath

class CheckSrtConfig:
  """Configuration class for CheckSrt."""
  
  def __init__(self):
    #Check current dir by default
    self.dir = [abspath('.')]
    
    #Don't be recursive by default
    self.recursive = False
    
    #Dont' be verbose by default
    self.verbose = False
    return
  
  def __unicode__(self):
    return str.format('CheckSrtConfig: Folders {0}; Recursive {1}; Verbose {2}.', self.dir, self.recursive, self.verbose)
    
  def __str__(self):
    return unicode(self).encode('utf-8')
pass
