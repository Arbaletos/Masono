import os
import sqlite3

def importu(datejo, datumo):
    db = sqlite3.connect(datejo)
    with open(datumo, 'w', encoding='utf-8') as writer:
        for res_id, dem_id, res in db.cursor().execute('select * from respondoj'):
            kun, dem = db.cursor().execute('select konteksto, demando from demandoj ' \
                                           'where dem_id=?', [dem_id]).fetchone()
            writer.write('\t'.join([kun, dem, res])+'\n')


if __name__=='__main__':
    importu('masono.db', 'el_datumo.tsv')

