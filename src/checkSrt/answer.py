#!/usr/bin/env python
#-*- coding: UTF-8 -*-

class CheckSrtAnswer():
  """Object that contains the results of a folder process.
  
  folder: the folder that has been processed.
  checkedFiles: the media files found.
  missingSubtitileFiles: the media files missing subtitles.
  subDirsAnswers: a list of aswers for subdirs on folder. Empty if recursivity is off, or there aren't subdirectories."""
  
  def __init__(self, folder = None, checkedFiles = [], missingSubtitileFiles = [], subDirsAnswers = []):
    self.folder = folder
    self.checkedFiles = checkedFiles
    self.missingSubtitileFiles = missingSubtitileFiles
    self.subDirsAnswers = subDirsAnswers
  
  def __unicode__(self):
    return str.format('CheckSrtAswer: Folders {0}\nChecked Files {1}\nMissing Subtitile Files {2}.', self.folder, self.checkedFiles, self.missingSubtitileFiles)
    
  def __str__(self):
    return unicode(self).encode('utf-8')
    
pass
