import sqlite3

con = sqlite3.connect('teaching_site.sqlite')
cur = con.cursor()
with open('сreate_db.sql', 'r') as db_script:
    script = db_script.read()
cur.executescript(script)
cur.close()
con.close()
