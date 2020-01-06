# SQLite is used for lightweight datastorage like in mobile applications etc.
import sqlite3
import json
from pathlib import Path

# ====================== WRITING TO DATABASE ==============================================
# (Select and uncomment whole section below.)

# # Reading data from movies.json file
# movies = json.loads(Path("movies.json").read_text())

# # Lets write this data into a database file
# # connect method will also create a DB file if it doesn't exist.and returns a connection object, which should be closed later like files.

# # connection_obj = sqlite3.connect("db.sqlite3")

# # so better to use "with" statement.
# with sqlite3.connect("db.sqlite3") as conn_obj:
#     # now we create an SQL command to perform create/read/update/delete (CRUD) operations.
#     command = "INSERT INTO Movies VALUES(?,?,?)"
#     # assumming there is a Table "Movies", ? are the placeholders for values to be passed.
#     for movie in movies:
#         conn_obj.execute(command, tuple(movie.values()))

#     # Once done with database operations, commit the changes.
#     conn_obj.commit()

#     # Code above this line on execution will throw ab error as we don't have any "Movies" table.
#     # We must first create a Database. Create a Table in our "db.sqlite3" file using SQLite DB Browser.
#     # Now upon executing above code , no error is thrown as we just created a Table "Movies",
#     # and also we can check newly added rows in DB Browser.


# ====================== READING FROM DATABASE ============================================

with sqlite3.connect("db.sqlite3") as conn_obj:
    command = "SELECT * FROM Movies"
    # command on execution will return a cursor object (iterable).
    cursor = conn_obj.execute(command)

    # for row in cursor:
    #     # a tuple corresponding to the values in the database row will be printed at each iteration.
    #     print(row)
    # # conn_obj.commit() # commit statement is only needed when writing to a database.

    # To fetch all the rows from cursor in one go, we can use fetchall method.
    movies = cursor.fetchall()
    print(movies)
    # as we saw in case of csv files, that once you iterate over it, index (or file-pointer) now point to EOF.
    # same is case for cursor, so then comment the for-loop code.
