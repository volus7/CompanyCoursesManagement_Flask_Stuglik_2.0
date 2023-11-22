import sqlite3

connection = sqlite3.connect("data/users.sqlite", check_same_thread=False)
cursor = connection.cursor()
# cursor.execute("SELECT * FROM teams")
# result = cursor.fetchone()
    
# data=cursor.execute('''INSERT INTO teams (id, name, manager_id) VALUES (2, 'Team F', '3')''')
# connection.commit()
# data=cursor.execute('''INSERT INTO users (id, username,role, password, team_id) VALUES (7, 'John', 'user','John', '2')''')
# connection.commit()
# data=cursor.execute('''INSERT INTO users (id, username,role, password, team_id) VALUES (8, 'Alex', 'user','Alex', '2')''')
# connection.commit()
# data=cursor.execute('''INSERT INTO users (id, username,role, password, team_id) VALUES (9, 'Jack', 'user','Jack', '2')''')
# connection.commit()

# data = cursor.execute("CREATE TABLE courses (id INTEGER PRIMARY KEY, name VARCHAR(255), correspondingTeamId INTEGER)")
# connection.commit()


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
