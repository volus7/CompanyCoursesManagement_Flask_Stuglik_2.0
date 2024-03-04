import sqlite3

connection = sqlite3.connect("data/users.sqlite", check_same_thread=False)
cursor = connection.cursor()
# cursor.execute("SELECT * FROM teams")
# result = cursor.fetchone()
    
# data=cursor.execute('''INSERT INTO teams (id, name, manager_id) VALUES (1, 'Team Super', '2')''')
# connection.commit()
#
# data=cursor.execute('''INSERT INTO teams (id, name, manager_id) VALUES (2, 'Team F', '3')''')
# connection.commit()
data=cursor.execute('''INSERT INTO users ( username,role, password, team_id) VALUES ('Joe', 'user','John', '3')''')
connection.commit()



# data=cursor.execute('''INSERT INTO users (username,role, password, team_id) VALUES ( 'man33', 'manager','man1', '0')''')
# connection.commit()
data=cursor.execute('''DELETE FROM users where username = 'aa' or username = 'Pan Chilary' ''')
connection.commit()
# #
# data = cursor.execute("CREATE TABLE courses (id INTEGER PRIMARY KEY, name VARCHAR(255), correspondingTeamId INTEGER)")
# connection.commit()
# data=cursor.execute('''INSERT INTO courses (id, name,correspondingTeamId) VALUES (1, 'CSS', '1')''')
# connection.commit()
# data=cursor.execute('''INSERT INTO courses (id, name,correspondingTeamId) VALUES (2, 'JS', '1')''')
# connection.commit()

# data = cursor.execute("CREATE TABLE courses_chapter (id INTEGER PRIMARY KEY, name VARCHAR(255), correspondingCourseId INTEGER)")
# connection.commit()
# data=cursor.execute('''INSERT INTO courses_chapter (id, name,correspondingCourseId) VALUES (1, 'Roz 1 - wstep', '1')''')
# connection.commit()
# data=cursor.execute('''INSERT INTO courses_chapter (id, name,correspondingCourseId) VALUES (2, 'Roz 2 - style wew i zew', '1')''')
# connection.commit()

# data = cursor.execute("CREATE TABLE courses_subsection (id INTEGER PRIMARY KEY, name VARCHAR(255), content VARCHAR(255), correspondingChapterId INTEGER)")
# connection.commit()
# data=cursor.execute('''INSERT INTO courses_subsection (id, name,content,correspondingChapterId) VALUES (1, '1.1 - witamy', 'Wtamy w naszym super kursie, nausczysz sie tu css', '1')''')
# connection.commit()
# data=cursor.execute('''INSERT INTO courses_subsection (id, name,content,correspondingChapterId) VALUES (2, '1.2 - co to css?','css to takie cos ', '1')''')
# connection.commit()
# data=cursor.execute('''INSERT INTO courses_subsection (id, name,content,correspondingChapterId) VALUES (3, '2.1 - co to style wew', 'style wew to te ktore sa  w srodku', '2')''')
# connection.commit()
# data=cursor.execute('''UPDATE courses_subsection SET name = 'Model pudełkowy CSS:', content= 'Model pudełkowy CSS opisuje układ i renderowanie elementów na stronie internetowej.' where id=3 ''')
# connection.commit()
data=cursor.execute('''UPDATE courses_chapter SET name = 'Rozdział 1: Wprowadzenie do CSS:'  where id=1 ''')
connection.commit()
data=cursor.execute('''UPDATE courses_chapter SET name = 'Rozdział 2: Właściwości CSS:'  where id=2 ''')
connection.commit()
print('\nColumns in courses_subsection table:')
data=cursor.execute('''SELECT * FROM courses_subsection''')
for column in data.description:
    print(column[0])

print('\nData in courses_subsection table:')
data=cursor.execute('''SELECT * FROM courses_subsection''')
for row in data:
    print(row)

print('\nColumns in courses_chapter table:')
data=cursor.execute('''SELECT * FROM courses_chapter''')
for column in data.description:
    print(column[0])

print('\nData in courses_chapter table:')
data=cursor.execute('''SELECT * FROM courses_chapter''')
for row in data:
    print(row)

print('\nColumns in COURSES table:')
data=cursor.execute('''SELECT * FROM courses''')
for column in data.description:
    print(column[0])

print('\nData in COURSES table:')
data=cursor.execute('''SELECT * FROM courses''')
for row in data:
    print(row)


print('\nColumns in TEAMS table:')
data=cursor.execute('''SELECT * FROM teams''')
for column in data.description:
    print(column[0])

print('\nData in TEAMS table:')
data=cursor.execute('''SELECT * FROM teams''')
for row in data:
    print(row)



print('\nColumns in USERS table:')
data=cursor.execute('''SELECT * FROM users''')
for column in data.description:
    print(column[0])

print('\nData in USERS table:')
data=cursor.execute('''SELECT * FROM users''')
for row in data:
    print(row)
