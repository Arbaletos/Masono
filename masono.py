import os
import sqlite3
import json
import random
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash 

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(dict(
  DATABASE=os.path.join(app.root_path, 'masono.db'),
  SECRET_KEY='disvolvigxa sxlosilo',
  USERNAME='admin',
  PASSWORD='derparol'
))

app.config.from_envvar('TODO_SETTINGS', silent=True)


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/sekv', methods=['GET'])
def sekva_demando():
  db = get_db()
  cur = list(db.execute('select dem_id, kunteksto, demando from demandoj'))
  cur = random.choice(cur)
  return json.dumps(list(cur))


@app.route('/send', methods=['POST'])
def sendu():
  datumo = json.loads(request.data.decode())
  ago('insert into respondoj (dem_id, respondo) values (?, ?)',
      [datumo['dem_id'], datumo['ago']])
  return redirect(url_for('sekva_demando'))


def ago(st, tem):
  db = get_db()
  cur = db.execute(st,tem)
  db.commit()
  

def connect_db():
  rv = sqlite3.connect(app.config['DATABASE'])
  rv.row_factory = sqlite3.Row
  return rv

def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def initdb_command():
    """Initializes the database."""
    init_db()
    print('Initialized the database.')

def get_db():
  if not hasattr(g, 'sqlite_db'):
    g.sqlite_db = connect_db()
  return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()



