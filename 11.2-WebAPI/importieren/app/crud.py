def create_item(cursor, name: str, description: str):
    cursor.execute("INSERT INTO items (name, description) VALUES (?, ?)", (name, description))
    return cursor.lastrowid

def get_item(cursor, item_id: int):
    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    return cursor.fetchone()
