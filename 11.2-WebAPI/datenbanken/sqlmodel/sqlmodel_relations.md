class Parent(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    children: List["Child"] = Relationship(back_populates="parent")


class Child(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    parent: Parent = Relationship(back_populates="children") # muss vor parent_id festgelegt werden
    parent_id: int = Field(default=None, foreign_key="parent.id")








# Set up the database engine and session
sqlite_file_name = "database.sqlite"
sqlite_url = f"sqlite:///{sqlite_file_name}"
#sqlite_url = "sqlite:///:memory:"  # SQLite in-memory database
engine = create_engine(sqlite_url, echo=True) # echo=True gibt Diagnosedaten auf der Konsole aus.

# Create the tables in the database
SQLModel.metadata.create_all(engine)


