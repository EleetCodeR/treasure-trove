# JSON = Java Script Object Notation, is a type of format used to represent data in human readable format.
import json
from pathlib import Path

# ================== CREATING/WRITING JSON FILE (DATA-SERIALIZATION) ===================================
# movies = [
#     {"id": 1, "title": "terminator", "year": 1989},
#     {"id": 2, "title": "kindergarten cop", "year": 1993},
# ]

# data = json.dumps(movies)
# print(data)
# Path("movies.json").write_text(data)

# ================== READING JSON FILE(DATA-DESERIALIZATION) ===================================
data = Path("movies.json").read_text()
movies = json.loads(data)
print(movies)
print(movies[0])
print(movies[0]["title"])
