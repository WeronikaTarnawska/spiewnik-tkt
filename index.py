#!/usr/bin/env python
#-*- coding: utf-8 -*-

import locale

locale.setlocale(locale.LC_COLLATE, "pl_PL.UTF-8")

def write_output():
  fout = open("out.tex", "w", encoding="utf8")

def get_titles():
  fin = open("spiewnik.tex", "r", encoding="utf8")
  titles = []
  page = 1
  ll = fin.readline()

  while ll:
    if ll.lstrip() and ll.lstrip()[0] == "%":
      pass
    elif "\\newpage" in ll:
      page+=1
    elif ll.lstrip() and ll.lstrip()[:8] == "\\section":
      ll=ll[ll.find('{')+1:ll.find('}')]
      if '\\foreignlanguage' in ll:
        ll="Salo"
      titles.append(f"{ll.strip()} {page}\\\\\n")
        
    ll = fin.readline()
  fin.close()
  return titles
    
    
def get_firstlines():
  fin = open("spiewnik.tex", "r", encoding="utf8")
  firstlines = []
  page = 1
  ll = fin.readline()

  while ll:
    if ll.lstrip() and ll.lstrip()[0] == "%":
      pass
    elif "\\newpage" in ll:
      page+=1
      
    elif ll.lstrip() and ll.lstrip()[:8] == "\\section":
      while ll.lstrip() and (ll.lstrip()[0] == '\\' or ll.lstrip()[0]=='~' or ll.lstrip()[0]=='%' or ll.lstrip()[0]=='}'):
        if "\\newpage" in ll:
          page+=1
        ll=fin.readline()
      ll = ll[:maxline]
      if '\\' in ll:
        ll=ll[:ll.find('\\')]
      else:
        x = ll.rfind(' ')
        if x>0:
          ll = ll[:x]
        ll =ll.strip().strip('\\')
      if '~' in ll:
        ll=ll[:ll.find('~')]
      if '(' in ll:
        ll=ll[:ll.find('(')]
      if '$' in ll:
        ll=ll[:ll.find('$')]
      if ll:
        firstlines.append(f"{ll.strip()} {page}\\\\\n") # max 35 znaków, przerwij na ostatniej spacji
        
    ll = fin.readline()
    
  fin.close()
  return firstlines
    
    
def get_refrains():
  fin = open("spiewnik.tex", "r", encoding="utf8")
  firstlines = []
  page = 1
  ll = fin.readline()

  while ll:
    if ll.lstrip() and ll.lstrip()[0] == "%":
      pass
    elif "\\newpage" in ll:
      page+=1
      
    elif ll.lstrip() and ll.lstrip()[:8] == "\\section":
      while ll.lstrip() and ll.lstrip()[:9] != '\\hspace*{':
        if "\\newpage" in ll and ll.lstrip()[0] != "%":
          page+=1
        ll=fin.readline()
      ll=ll[ll.find('}')+1:]
      ll = ll[:maxline]
      if '\\' in ll:
        ll=ll[:ll.find('\\')]
      else:
        x = ll.rfind(' ')
        if x>0:
          ll = ll[:x]
        ll =ll.strip().strip('\\')
      if '~' in ll:
        ll=ll[:ll.find('~')]
      if '(' in ll:
        ll=ll[:ll.find('(')]
      if '$' in ll:
        ll=ll[:ll.find('$')]
      if ll:
        firstlines.append(f"{ll.strip()} {page}\\\\\n") # max 35 znaków, przerwij na ostatniej spacji
        
    ll = fin.readline()
    
  fin.close()
  return firstlines

maxline=32
a, b, c = get_firstlines(), get_refrains(), get_titles()
index = a+b+c
index.sort(key=lambda x: locale.strxfrm(x))

with open('index-py.txt', "w", encoding="utf8") as fout:
  fout.write("~\\\\\n")
  prev = '.'
  for i in index:
    if not i[0].isnumeric() and i[0]!="'" and i[0].upper() != prev:
      prev=i[0].upper()
      fout.write("\\\\\n{\\footnotesize \\textbf{"+f"{prev}"+"\\\} }\n")
    fout.write(i)
    



# Salo 135 - manualnie
