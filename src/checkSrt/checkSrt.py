#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import os
import re
from config import CheckSrtConfig
from answer import CheckSrtAnswer

class CheckSrt:
  """Script to check if one (or more than one) folder contains subtitle files (*.srt) for all media files."""
  
  def __init__(self, options=None):
    if(options != None):
      #If CheckSrtConfig has been passed use it.
      self.options = options
    else:
      #If no option has been passed use default values.
      self.options = CheckSrtConfig()
    return
  
  def __verboseOutput(self, message):
    """Print message if verbose mode is activated."""
    if(self.options.verbose):
      print message
    return
  
  def checkFolders(self):
    """Check in a list of folders if all of *.mkv, *.avi and *.mp4 has a matching *.srt file.
    Return a list of CheckSrtAnswer with result of process folder(s)."""
    
    answers = []
    for folder in self.options.dir:
      answers.append(self.__checkFolder(folder))
    return answers
  
  def __checkFolder(self, folder):
    """Check in a folder if all of *.mkv, *.avi and *.mp4 has a matching *.srt file.
    Return a CheckSrtAnswer with result of process folder(s)."""
    
    if(os.path.exists(folder) == False):
      raise IOError(str.format('Folder {} does not exists.', folder))
    self.__verboseOutput(str.format('Checking srt files on {0}.', folder))
    
    answer = CheckSrtAnswer()
        
    #Get subdir and files in the folder directory
    root, subDirs, files = os.walk(folder).next()
    
    answer.folder = folder    
    
    if self.options.recursive:
      subDirs.sort()
      for subDir in subDirs:
        answer.subDirsAnswers.append(self._checkFolder(os.path.join(folder, subDir)))
    
    files.sort()
    for item in files:
      fullItemName = os.path.join(folder, item)
      if self.__isMediaFile(fullItemName):
        #Add the file to the tested file list
        answer.checkedFiles.append(fullItemName)
        
        #Do the subtitle verification
        if not self.__checkSrtFile(fullItemName):
          #Add the file to the list of missing subtitile file.
          answer.missingSubtitileFiles.append(fullItemName)
    return answer
  
  def __isMediaFile(self, filePath):
    """Check if a path represents a media file (mkv, avi or mp4)."""
    #Prepare the regex
    regex = '.*\\.(mkv|avi|mp4)'
    reText = re.compile(regex)

    #Text the regex    
    return reText.match(filePath)
  
  def __checkSrtFile(self, filePath):
    """Check if the filePath has a corresponding subtitile file."""
    self.__verboseOutput(str.format('Checking subtitle for {0}', filePath))
    srtFile = os.path.splitext(filePath)[0] + '.srt'
    return os.path.exists(srtFile)
    
pass
