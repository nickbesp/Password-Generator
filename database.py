import sqlite3 as sql

def getData():
    con = sql.connect('data.db')
    cur = con.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, login TEXT, password TEXT, shifr TEXT)')
    logins = dict()
    length = len(list(cur.execute('SELECT id FROM users')))
    for i in range(length):
        login = cur.execute(f'SELECT login FROM users WHERE id == {i + 1}').fetchone()[0]
        password = cur.execute(f'SELECT password FROM users WHERE id == {i + 1}').fetchone()[0]
        shifr = cur.execute(f'SELECT shifr FROM users WHERE id == {i + 1}').fetchone()[0]
        logins[login] = [password, shifr]

    con.commit()
    cur.close()
    con.close()

    return logins

def saveData(logins):
    con = sql.connect('data.db')
    cur = con.cursor()

    cur.execute('DROP TABLE IF EXISTS users')
    cur.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, login TEXT, password TEXT, shifr TEXT)')
    
    for login in logins:
        elem = logins[login]
        log = login
        passw = str(elem.somelock)
        shifr_list = elem.someshifr
        shif = str()
        for i in shifr_list:
            shif += i + ' '
        cur.execute('INSERT INTO users(login, password, shifr) VALUES(?, ?, ?)', [log, passw, shif])

    con.commit()
    cur.close()
    con.close()