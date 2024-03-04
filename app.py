import hashlib
import sqlite3
from cgitb import text

from flask import Flask, request, render_template, redirect, session, abort, flash
from flask_session import Session
from datetime import timedelta

app = Flask(__name__)
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = '10764a32f083da83643be57e1458adfd'
app.config['SESSION_PERMANENT'] = True
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=20)

Session(app)
 
connection = sqlite3.connect("data/users.sqlite", check_same_thread=False)
cursor = connection.cursor()

firstTime = 0

@app.route("/login", methods=["POST", "GET"])
def login():
    global firstTime
    session["localization"] = "login"
    if firstTime == 0:
        session["correct"] = "Correct"
    if request.method == "POST":
        username = request.form.get('username')
        cursor.execute("SELECT password FROM users WHERE username=?", [username])
        result = cursor.fetchone()
        if not result:

            session["correct"] = "noCorrect"
            firstTime = 1
            return redirect('/login')
        else:
            password_hash, = result
            if hashlib.md5(request.form.get('password').encode()).hexdigest() == password_hash:
                session["username"] = request.form.get("username")
                cursor.execute("SELECT role, name FROM users INNER JOIN teams on team_id=teams.id WHERE username=?",
                               [session["username"]])
                session["role"], session["team_name"] = cursor.fetchone()

                session['username'] = username
                return redirect("/")
            else:
                session["correct"] = "noCorrect"
                firstTime = 1
                return redirect('/login')
    return render_template("login.html", correct=session["correct"])


@app.route('/logout')
def logout():
    session.clear()
    session["correct"] = "noCorrect"
    return render_template("logout.html")

@app.route('/')
def index():
    session["localization"] = "index"
    if not session.get("username"):
        return redirect("/login")

    if session.get("role") == 'manager':
        cursor.execute("SELECT role, name FROM users INNER JOIN teams on team_id=teams.id WHERE username=?",
                       [session["username"]])
        
    cursor.execute("SELECT id, name, correspondingTeamId FROM courses")
    courses = cursor.fetchall()

    return render_template('index.html', username=session["username"], role=session.get("role"),
                           team_name=session.get("team_name"), courses=courses)

@app.route('/manageCourses')
def manage_courses():
    session["localization"] = "manage_courses"
    if not session.get("username"):
        return redirect("/login")
    if session.get("role") != 'admin':
        abort(403)


    cursor.execute("SELECT id, name, correspondingTeamId FROM courses")
    courses = cursor.fetchall()

    cursor.execute("SELECT username, teams.id FROM users INNER JOIN teams on users.id=manager_id WHERE role=='manager'")
    managers = cursor.fetchall()

    cursor.execute("SELECT id, name, correspondingCourseId FROM courses_chapter")
    courses_chapter = cursor.fetchall()

    cursor.execute("SELECT * FROM courses_subsection")
    courses_subsection = cursor.fetchall()
    return render_template('manageCourses.html', courses_subsection=courses_subsection,courses_chapter=courses_chapter,courses=courses, managers=managers, role=session.get("role"))


@app.route('/manageUsers')
def manage_users():
    session["localization"] = "manage_users"
    if not session.get("username"):
        return redirect("/login")
    if session.get("role") != 'manager' and session.get("role") != 'admin':
        abort(403)

    cursor.execute("SELECT username, team_id, id FROM users WHERE role=='user'")
    users = cursor.fetchall()
    teams = []
    cursor.execute("SELECT name, team_id FROM teams INNER JOIN users on teams.id=users.team_id WHERE role=='user'")
    teams = cursor.fetchall()

    cursor.execute("SELECT username, teams.id FROM users INNER JOIN teams on users.id=manager_id WHERE role=='manager'")
    managers = cursor.fetchall()



    # Utworzenie zbioru, aby usunąć powtórki
    teams2 = set(teams)
    # Konwersja zbioru z powrotem na listę
    teams = list(teams2)

    return render_template('manageUsers.html', users=users, teams=teams, managers=managers, role=session.get("role"))


@app.route('/manageManagers', methods=['GET', 'POST'])
def manege_managers():
    session["localization"] = "manege_managers"
    if not session.get("username"):
        return redirect("/login")
    if session.get("username") != 'admin':
        abort(403)

    if request.method == 'POST':

        manager_name = request.form['manager_name']
        team_name = request.form['team_name']
        manager_password = request.form['manager_password']

        sql = "INSERT INTO users (username, role, password, team_id) VALUES (:manager_name, 'manager', :manager_password, 0)"
        cursor.execute(sql, {"manager_name": manager_name, "manager_password": manager_password})
        connection.commit()

        cursor.execute("SELECT users.username, teams.name FROM USERS, TEAMS WHERE users.role='manager' and users.id = teams.manager_id")

        managers = cursor.fetchall()



        return render_template('manageManagers.html', managers=managers, role=session.get("role"))






    # cursor.execute("SELECT users.username, teams.name FROM USERS, TEAMS WHERE users.role='manager' and users.id = teams.manager_id")
    cursor.execute("SELECT users.username FROM USERS WHERE users.role='manager'")
    
    managers = cursor.fetchall()


    return render_template('manageManagers.html', managers=managers, role=session.get("role"))

#zarządzanie pracownikami teamami itp

@app.route('/deleteTeam', methods=['DELETE'])
def deleteTeam():

    data = request.get_json()
    team_id = data.get('teamName')
    
    
    sql = f"DELETE FROM teams WHERE id = {team_id}"
    cursor.execute(sql, {"team_id": team_id})
    connection.commit()
    return redirect("/manageUsers")

@app.route('/deleteUser/<string:user_id>', methods=['GET'])
def deleteUser(user_id):

    sql = "UPDATE users SET team_id= -1 WHERE id = :user_id"
    cursor.execute(sql, {"user_id": user_id})
    connection.commit()
    return redirect("/manageUsers")


@app.route('/kontakt')
def kontakt():
    return render_template("kontakt.html", username=session["username"], role=session.get("role"))

if __name__ == '__main__':
    app.run(debug=True)


