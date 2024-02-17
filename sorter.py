#!/usr/bin/env python
#-*- coding: utf-8 -*-

import locale
import sys

locale.setlocale(locale.LC_COLLATE, "pl_PL.UTF-8")

if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: python3 sorter.py [infile] [outfile]")
    exit()
  fin = open(sys.argv[1], "r", encoding="utf8")
  fout = open(sys.argv[2], "w", encoding="utf8")
  toc = open("toc.txt", "w", encoding="utf8")
  sections = []
  line = ":)"
  prevline = ""
  cnt = 0

  # skip preample
  while line[:8] != "\\section":
    line = fin.readline()
    if line[:8]=="\\section":
      break
    fout.write(line)

  sections.append([line, "\\newpage\n"+line])

  while line:
    line = fin.readline()
    if line[:8] == "\\section":
      cnt += 1
      sections.append([line, line])
    # if line[:8] == "\\section":
    #   cnt += 1
    #   sections.append([line, "\\newpage\n"+line])
    # elif line[:8] == "\\newpage":
    #   continue
    elif line == "\n" and prevline=="\n":
      continue
    elif line[:1] == "%":
      continue
    elif line[:14] == "\\end{document}":
      print(":)")
      break
    else:
      sections[cnt][1]+=line
    prevline=line
      
  sections.sort(key=lambda x: locale.strxfrm(x[0]))

  for s in sections:
    fout.write(s[1])
    line=s[0]
    toc.write(line[line.find('{')+1:line.find('}')]+'\n')
    
  fout.write("\\end{document}\n")

  fin.close()
  fout.close()
  toc.close()