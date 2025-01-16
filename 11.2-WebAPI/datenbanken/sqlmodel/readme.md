# SQLModel


## 1:n Beziehung
Hier gibt es zu jedem Eintrag *(=1)* in der Tabelle `Parent` 0, 1 oder mehrere *(=n)* Einträge in der Tabelle Child.

```python
class Parent(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    children: List["Child"] = Relationship(back_populates="parent")
```

```python
class Child(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    parent_id: int = Field(foreign_key="parent.id")
```

Auch wenn die Klasse `Parent` groß geschrieben wird, muss der Verweis im `foreign_key` klein geschrieben werden.
