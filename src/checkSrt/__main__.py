#!/usr/bin/env python
#-*- coding: UTF-8 -*-

"""2012  Diego Rocha <diego@diegorocha.com.br>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>."""

import os
from argparse import ArgumentParser, Action, ArgumentTypeError
from config import CheckSrtConfig
from checkSrt import CheckSrt

class ValidDirAction(Action):
  """A custom argparse.Action to validate directories."""
  
  def __call__(self, parser, namespace, values, option_string=None):
    """Verify if all arguments passed are valid directories."""
    for i, directory in enumerate(values):
      if not os.path.isdir(directory):
        raise ArgumentTypeError(str.format("{0} is not a valid directory.", directory))
      if os.access(directory, os.R_OK):
        values[i] = os.path.abspath(directory)
      else:
        raise ArgumentTypeError(str.format("{0} is not a readable dir.", directory))
    setattr(namespace, self.dest, values)
    return
    
pass

if __name__ == '__main__':
  config = CheckSrtConfig()
  
  #Handle arguments (input)
  argumentParser = ArgumentParser(description = CheckSrt.__doc__, epilog='Author: Diego Rocha <diego@diegorocha.com.br>')
  argumentParser.add_argument('-r', '--recursive', action = 'store_true', dest = 'recursive', help = 'check folders recursively')
  argumentParser.add_argument('-v', '--verbose', action = 'store_true', dest = 'verbose', help = 'enable verbose output')
  argumentParser.add_argument('dir', action = ValidDirAction, nargs='*', help='directory(ies) to check', default=['.'])
  argumentParser.parse_args(namespace = config)
  
  #Process
  checkSrt = CheckSrt(config)
  answer = checkSrt.checkFolders()
  
  #Output
  print answer
