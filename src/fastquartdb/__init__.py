"""FastQuartDB - A Fast and Efficient Database Management System

FastQuartDB is a lightweight database management system designed for fast data operations
and simple integration with Python applications.

Example:
    >>> from fastquartdb import create_basemodel, Column
    >>> class User(create_basemodel("./database.db", create_table=True)):
    ...     name = Column("STRING", index=True))
    ...     age = Column("INTEGER", index=False))
    ...  
    >>> await User.fetch(filter={"age": 30})

For more information, visit: https://github.com/PeeeterS/FastQuartDB
"""

from fastquartdb.utils import create_basemodel, Column

__version__ = "0.1.0"
__author__ = "PeeeterS"
__license__ = "MIT"
__copyright__ = "Copyright 2025 PeeeterS"

# Define the public API
__all__ = [
    "create_basemodel",
    "Column",
    "__version__",
    "__author__",
    "__license__",
]
