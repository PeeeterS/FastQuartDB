# FastQuartDB

**Asynchronous lightweight SQLite toolkit** for small Python web projects (Quart, FastAPI, aiohttp).  
Built for developers who want *database power without ORM overhead*.

---

## Features

- **Async I/O** — built on `aiosqlite`
- **Optional FileLock** — safe access across multiple processes
- **Dynamic BaseModel system** — define models as plain Python classes
- **Auto table creation** — create tables on first import or at engine init
- **Singleton DB access** — one shared async connection throughout your app
- **Simple CRUD** — perform `fetch`, `insert`, `update`, `delete` with clean syntax
- **Operator filters** — use SQL operators dynamically in filters

---

## Installation

```bash
pip install fastquartdb
```

or if you use [uv](https://github.com/astral-sh/uv):

```bash
uv add fastquartdb
```

---

## Initialization

Start the database engine once at application startup:

```python
from fastquartdb import AsyncDatabaseManager

await AsyncDatabaseManager.init_engine("data/mydb.sqlite", use_filelock=True)
```

After that, access it anywhere with:

```python
db = AsyncDatabaseManager.get()
```

---

## Defining Models

Every model inherits from `BaseModel`.  
You define columns using the lightweight `Column` helper.

```python
from fastquartdb import BaseModel, Column

class User(BaseModel):
    id = Column("INTEGER", primary_key=True)
    username = Column("TEXT", nullable=False)
    age = Column("INTEGER")
```

Each subclass automatically gets a matching table (`user` by default).

---

## CRUD Operations

### Insert

```python
await User.insert({"username": "Alice", "age": 30})
```

### Fetch (with operators)

```python
users = await User.fetch(
    filters={"age": [(">", 20), ("<", 40)]},
    columns=["id", "username"]
)
```

### Update

```python
await User.update(
    data={"age": 31},
    filters={"username": [("=", "Alice")]}
)
```

### Delete

```python
await User.delete(filters={"age": [("<", 18)]})
```

---

## FileLock Mode

Enable safe access if multiple processes may touch the same SQLite file:

```python
await AsyncDatabaseManager.init_engine("mydb.sqlite", use_filelock=True)
```

Each query is automatically wrapped in a file-based async lock.

---

## Example Integration with Quart

```python
from quart import Quart, jsonify
from fastquartdb import AsyncDatabaseManager, BaseModel, Column

class User(BaseModel):
    id = Column("INTEGER", primary_key=True)
    name = Column("TEXT", nullable=False)

app = Quart(__name__)

@app.before_serving
async def init_db():
    await AsyncDatabaseManager.init_engine("data/app.db")

@app.route("/users")
async def list_users():
    return jsonify(await User.fetch())

if __name__ == "__main__":
    app.run()
```

---

## Design Philosophy

FastQuartDB aims to be:
- **smaller** than SQLAlchemy
- **simpler** than ORMs
- **faster** to bootstrap for small async projects
- **flexible** for use with Quart, FastAPI, or scripts

No declarative meta, no complex migrations — just tables, data, and async Python.

---

## License

MIT © 2025 PeeeterS

---

## Future Ideas

- `JOIN` and aggregation support  
- `upsert()` helper  
- `BaseModel.json()` serialization  
- `FastQuartDB CLI` for inspecting SQLite files
