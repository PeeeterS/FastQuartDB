from fastquartdb.base_model import BaseModel
from pathlib import Path
from typing import Type

def create_basemodel(
        sqlite_path: str|Path, 
        create_table: bool = True,
        use_filelock: bool = True, 
        filelock_timeout: int = 10
        ) -> Type[BaseModel]:
    return 

class Column:
    pass