import sqlite3 as sql

# con = sql.connect('data.db')
# cur = con.cursor()

# cur.execute('DROP TABLE users')
# cur.execute('CREATE TABLE users(id INTEGER PRIMARY KEY, login TEXT, password TEXT, shifr TEXT)')
# cur.execute('''INSERT INTO users(login, password, shifr) VALUES("nickbesp", "1234", "1q 2a zxc 4x 5c V8 7b 8n 9m _l 1p 2o I3 u_ 5y 6t 7r 8e 9w 0s 1d 2f 3g 4h 5j 6k _7 8A Q_ G1 LOL 4F 5j 6z 7p 8I 9t QbZ")''')

# con.commit()
# cur.close()
# con.close()

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

    log_list = cur.execute('SELECT login FROM users').fetchall()
    for i in range(len(log_list)):
        log_list[i] = log_list[i][0]
    print(log_list)
    for login in logins:
        if login not in log_list:
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