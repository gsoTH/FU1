import os
import sqlite3


def get_absolute_path(relative_path: str) -> str:
    # Abfragen, in welchem Verzeichnis dieses Skript liegt.
    scriptdir: str = os.path.dirname(__file__)

    # Beide Pfade zusammensetzen
    combined_path: str = os.path.join(scriptdir, relative_path)
    
    #print(combined_path)
    # --> C:\repos\flaskShowcase\datenbanken\db/example_db.sqlite

    # Pfad normalsieren
    # also vereinheitlichen, an Betriebssystem anpassen
    absolute_path = os.path.normcase(combined_path)
    
    #print(absolute_path)
    # --> c:\repos\FU1\datenbanken\db\example_db.sqlite

    
    return absolute_path


if __name__ == "__main__":
    relative_path = 'db/example_db.sqlite'
    db_path = get_absolute_path(relative_path)
    
    con: sqlite3.Connection = sqlite3.connect(db_path)
    cursor: sqlite3.Cursor = con.execute("SELECT * FROM stats")
    print(cursor.fetchall())
