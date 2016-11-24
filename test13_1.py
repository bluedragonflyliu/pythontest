import sqlite3
def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = '0'
    return float(value)
conn = sqlite3.connect("food.db")
cur = conn.cursor()

curs.execute('''
    CREATE TABLE food(
        id TEXT PRIMARY KEY,
        desc TEXT,
        water FLOAT,
        kcal FLOAT,
        protein FLOAT,
        fat FLOAT,
        ash FLOAT,
        carbs FLOAT,
        fiber FLOAT,
        sugar FLOAT
    )
''')

field_count = 10
markers = ', '.join(['%s']*field_count)

query = 'INSERT INTO food VALUES(?,?,?,?,?,?,?,?,?,?)'

for line in open('ABBREV.txt'):
    fields = line.sqlit('^')
    vals = [convert(f) for f fields[:field_count]]
    curs.execute(query,vals)

conn.commit()
conn,close()
