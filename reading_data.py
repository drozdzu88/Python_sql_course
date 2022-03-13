from pw import password as pw
from db_functions import create_server_connection, create_db_connection, read_query, execute_query, execute_list_query
import pandas as pd

db = "school_2"
connection = create_server_connection("localhost", "root", pw)

# %%
# Simple query to see how it works.
q1 = """
SELECT *
FROM teacher;
"""

connection = create_db_connection('localhost', 'root', pw, db)
results = read_query(connection, q1)

for result in results:
    print(result)
    
# %%
q5 = """
SELECT course.course_id, course.course_name, course.language, client.client_name, client.address
FROM course
JOIN client
ON course.client = client.client_id
WHERE course.in_school = FALSE;
"""

connection = create_db_connection('localhost', 'root', pw, db)
results = read_query(connection, q5)

for result in results:
    print(result)
    
# %%
# Formating Output into a List
from_db = []

for result in results:
    result = result
    from_db.append(result)
    
print(from_db)

# %%
# The same using list comprehension and result is returned as list not tuple.

from_db = [list(result) for result in results]
print(from_db)

# %%
# Formatting Output into a pandas DataFrame
from_db = [list(result) for result in results]
columns = ['course_id', 'course_name', 'language', 'client_name', 'address']
df = pd.DataFrame(from_db, columns=columns)

display(df)
# %%
# Update record

update = """
UPDATE client
SET address = '23 Fingiertweg, 14534 Berlin'
WHERE client_id = 101;
"""

connection = create_db_connection('localhost', 'root', pw, db)
execute_query(connection, update)

# %%
# Delete records
delete_course = """
DELETE FROM course
WHERE course_id = 20;
"""
connection = create_db_connection('localhost', 'root', pw, db)
execute_query(connection, delete_course)
# %%
# Createing records from List

sql = '''
    INSERT INTO teacher (teacher_id, first_name, last_name, language_1, language_2, dob, tax_id, phone_no) 
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    
val = [
    (7, 'Hank', 'Dodson', 'ENG', None, '1991-12-23', 11111, '+491772345678'), 
    (8, 'Sue', 'Perkins', 'MAN', 'ENG', '1976-02-02', 22222, '+491443456432')
]

connection = create_db_connection("localhost", "root", pw, db)
execute_list_query(connection, sql, val)

# %%
q1 = """
SELECT *
FROM teacher;
"""
connection = create_db_connection("localhost", "root", pw, db)
results = read_query(connection, q1)

for result in results:
    print(result)





































