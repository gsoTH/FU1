#
#   Quelle: https://docs.python.org/3/library/sqlite3.html#sqlite3-placeholders
#   Um Typehints erweitert.
#

import sqlite3

# erstellt eine in-memory-Datenbank
con: sqlite3.Connection = sqlite3.connect(":memory:")
cur: sqlite3.Cursor = con.execute("CREATE TABLE lang(name, first_appeared)")

# named style
# For the named style, parameters must be an instance of a dict (or a subclass)
named_parameter: tuple = (
    {"name": "C", "year": 1972},
    {"name": "Fortran", "year": 1957},
    {"name": "Python", "year": 1991},
    {"name": "Go", "year": 2009},
)

# Mehr als ein Statement ausführen
cur.executemany("INSERT INTO lang VALUES(:name, :year)", named_parameter)


# questionmark (qmark) style
# For the qmark style, parameters must be a sequence whose length must match the number of placeholders
anon_parameter = [1972]

# Ein einzelnes Statement ausführen
cur.execute("SELECT * FROM lang WHERE first_appeared = ?", anon_parameter)

print(cur.fetchall())   # --> [('C', 1972)]