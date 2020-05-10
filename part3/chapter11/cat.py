import sys
import fileinput

with fileinput.FileInput(files=sys.argv[1:]) as f:
  for line in f:
      print(line, end="")
