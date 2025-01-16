# Datenbanken
Beispiele zur Anbindung einer Datenbank mit eigenen Funktionen.

| Skript                                               | Beschreibung                                                                     |
|------------------------------------------------------|----------------------------------------------------------------------------------|
| [sqlite_insert_execute.py](sqlite_insert_execute.py) | Eine oder mehrere SQL-Anweisungen ausführen und Parameter einsetzen.             |
| [sqlite_relative_path.py](sqlite_relative_path.py)   | Datenbank-Import-Error verhindern indem relative Dateipfade absolut werden.      |
| [sqlite_row_factory.py](sqlite_row_factory.py)       | Beispiele, wie die Rückaben von SQL-Abfragen in Python-Typen umgewandelt werden. |


## Auszug Dokumentation von sqlite3
[Quelle](https://docs.python.org/3/library/sqlite3.html#connection-objects)

### class sqlite3.Connection
Each open SQLite database is represented by a Connection object, which is created using sqlite3.connect(). 
Their main purpose is creating Cursor objects.

### class sqlite3.Cursor
A cursor can be viewed as a pointer to one row in a set of rows. 
The cursor can only reference one row at a time, but can move to other rows of the result set as needed. 
To use cursors you need to do the following:
1. Declare a cursor that defines a result set
2. Open the cursor to establish the result set
3. Fetch the data into local variables as needed from the cursor, one row at a time
4. Close the cursor when done

A [Cursor](https://docs.python.org/3/library/sqlite3.html#sqlite3.Cursor) instance has the following attributes and methods:
#### execute(sql, parameters=())
Execute a single SQL statement, optionally binding Python values using placeholders.

Parameters
- sql (str) – A single SQL statement.
- parameters (dict | sequence) – Python values to bind to placeholders in sql. A dict if named placeholders are used. A sequence if unnamed placeholders are used. See How to use placeholders to bind values in SQL queries.

#### executemany(sql, parameters)
For every item in parameters, repeatedly execute the parameterized DML SQL statement sql.

Parameters:
- sql (str) – A single SQL DML statement.
- parameters (iterable) – An iterable of parameters to bind with the placeholders in sql.

#### executescript(sql_script: str)

#### fetchone()
If row_factory is None, return the next row query result set as a tuple. Else, pass it to the row factory and return its result. Return None if no more data is available.

#### fetchall()
Return all (remaining) rows of a query result as a list. Return an empty list if no rows are available.

#### lastrowid
Read-only attribute that provides the row id of the last inserted row. It is only updated after successful INSERT or REPLACE statements using the execute() method. For other statements, after executemany() or executescript(), or if the insertion failed, the value of lastrowid is left unchanged. The initial value of lastrowid is None.

#### row_factory
By default, sqlite3 represents each row as a tuple. If a tuple does not suit your needs, you can use the sqlite3.Row class or a custom row_factory.
While row_factory exists as an attribute both on the Cursor and the Connection, it is recommended to set Connection.row_factory, so all cursors created from the connection will use the same row factory.
[See How to create and use row factories for more details.](https://docs.python.org/3/library/sqlite3.html#sqlite3-howto-row-factory)