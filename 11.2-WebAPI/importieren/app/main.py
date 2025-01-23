from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app import crud, db

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

@app.post("/items/")
def create_item(item: Item):
    db_connection = db.get_db_connection()
    db_cursor = db_connection.cursor()
    
    item_id = crud.create_item(db_cursor, item.name, item.description)
    
    db_connection.commit()
    db_connection.close()
    
    return {"id": item_id, "name": item.name, "description": item.description}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    db_connection = db.get_db_connection()
    db_cursor = db_connection.cursor()
    
    item = crud.get_item(db_cursor, item_id)
    
    db_connection.close()
    
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    return {"id": item[0], "name": item[1], "description": item[2]}
