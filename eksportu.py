import os
import sqlite3

def eksportu(datumo, datejo):
  db = sqlite3.connect(datejo)
  for line in open(datumo,'r',encoding='utf-8'):
      kunteksto, demando = line.strip().split('\t')
      db.cursor().execute('insert into demandoj(konteksto, demando) values(?, ?)', 
                          [kunteksto, demando])
  db.commit()


if __name__=='__main__':
    eksportu('en_datumo.tsv', 'masono.db')
