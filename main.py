from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from random import shuffle
from database import *

def addUser(login, lock):
    global logins
    shuffle(shifr1)
    logins[login] = Users(lock, shifr1)
    saveData(logins)
    pass

def ADWindow():
    adWin = QWidget()
    adWin.setWindowTitle('Admin')
    adWin.setFixedSize(300, 250)

    getListButton = QPushButton('Список пользователей')
    #getListButton.clicked.connect(showlistwin)
    addButton = QPushButton('Добавить пользователя')
    addButton.clicked.connect(showaddwin)
    deleteButton = QPushButton('Удалить пользователя')
    #deleteButton.clicked.connect(showdelwin)
    backButton = QPushButton('Назад')
    deleteButton.clicked.connect(showlogAd)

    v_line = QVBoxLayout()
    v_line.addWidget(getListButton, alignment=Qt.AlignCenter)
    v_line.addWidget(addButton, alignment=Qt.AlignCenter)
    v_line.addWidget(deleteButton, alignment=Qt.AlignCenter)
    v_line.addWidget(backButton, alignment=Qt.AlignCenter)
    
    adWin.setLayout(v_line)

    return adWin

def CHwindow():
    global userPassword
    chWin = QWidget()
    chWin.setWindowTitle('Админский вход')
    chWin.setFixedSize(200, 200)

    title = QLabel('Введите пароль')

    userPassword = QLineEdit('')
    userPassword.setPlaceholderText('Пароль')

    confButton = QPushButton('Подтвердить')
    confButton.clicked.connect(adCheck)

    v_line = QVBoxLayout()
    v_line.addWidget(title, alignment=Qt.AlignCenter)
    v_line.addWidget(userPassword, alignment=Qt.AlignCenter)
    v_line.addWidget(confButton, alignment=Qt.AlignCenter)

    chWin.setLayout(v_line)

    return chWin

def ADDwindow():
    global newLogin, newPassword

    addWin = QWidget()
    
    newLogin = QLineEdit()
    newLogin.setPlaceholderText('Логин')
    newPassword = QLineEdit()
    newPassword.setPlaceholderText('Пароль')

    confButton = QPushButton('Подтвердить')
    confButton.clicked.connect(addUserAd)

    v_line = QVBoxLayout()
    v_line.addWidget(newLogin, alignment=Qt.AlignCenter)
    v_line.addWidget(newPassword, alignment=Qt.AlignCenter)
    v_line.addWidget(confButton, alignment=Qt.AlignCenter)

    addWin.setLayout(v_line)

    return addWin

def LISTwindow():
    pass

def DELwindow():
    pass

def addUserAd():
    global newLogin, newPassword, logins

    log = newLogin.text()
    pas = newPassword.text()
    newLogin.clear()
    newPassword.clear()
    addWindow.hide()

    if log in logins or len(log) == 0 or len(pas) == 0:
        addFalse()
    else:
        addUser(log, pas)
        messWin = QMessageBox()
        messWin.setWindowTitle('Accepted')                                 #addTrue
        messWin.setText('Пользователь добавлен!')
        messWin.exec()

    adminWin.show()

def addFalse():
    messWin = QMessageBox()
    messWin.setWindowTitle('Error')
    messWin.setText('Пользователь уже существует или логин или пароль - пусты!')
    messWin.exec()

def adCheck():
    currPass = userPassword.text()
    userPassword.clear()
    checkWin.hide()
    if currPass == '1234 ':
        adminWin.show()
    else:
        accessFalse()
        logWin.show()

def accessFalse():
    messWin = QMessageBox()
    messWin.setWindowTitle('Error')
    messWin.setText('Доступ запрещен!')
    messWin.exec()

def showAdmin():
    adminWin.show()

def showaddwin():
    adminWin.hide()
    addWindow.show()

def showdelwin():
    pass

def showlogAd():
    adminWin.hide()
    logWin.show()

def showlistwin():
    pass

def LOGwindow():
    global logLine, passLine, errTitle

    logWin = QWidget()
    logWin.setWindowTitle('Password Generator')
    logWin.setFixedSize(400, 200)

    title = QLabel('Добро пожаловать! Введите свой логин и пароль!')
    logtitle = QLabel('Логин:')
    passtitle = QLabel('Пароль:')
    errTitle = QLabel('')

    logLine = QLineEdit('')

    passLine = QLineEdit('')

    enterButton = QPushButton('Вход')
    enterButton.clicked.connect(logCheck)

    adEnterButton = QPushButton('Админ')
    adEnterButton.clicked.connect(showCheck)
    
    h_line1 = QHBoxLayout()
    h_line1.addWidget(logtitle, alignment = Qt.AlignRight)
    h_line1.addWidget(logLine, alignment = Qt.AlignLeft)

    h_line2 = QHBoxLayout()
    h_line2.addWidget(passtitle, alignment = Qt.AlignRight)
    h_line2.addWidget(passLine, alignment = Qt.AlignLeft)

    v_line = QVBoxLayout()
    v_line.addWidget(title, alignment = Qt.AlignCenter)
    v_line.addLayout(h_line1)
    v_line.addLayout(h_line2)
    v_line.addWidget(enterButton, alignment = Qt.AlignCenter)
    v_line.addWidget(adEnterButton, alignment = Qt.AlignCenter)
    v_line.addWidget(errTitle, alignment = Qt.AlignCenter)

    logWin.setLayout(v_line)

    return logWin

def showlog():
    logLine.clear()
    passwLine.clear()
    passWin.hide()
    logWin.show()
    nameLine.clear()

def logCheck():
    global login, lock
    login = logLine.text()
    lock = passLine.text()
    if login in logins:
        if not logins[login].somelock == lock:
            errTitle.setText('Неправильный логин или пароль!')
        else:
            showpass()
    else:
        addUser(login, lock)
        showpass()

def showCheck():
    passLine.clear()
    errTitle.setText('')
    logWin.hide()
    checkWin.show()

def PASSwindow():
    global nameLine, passwLine

    passWin = QWidget()
    passWin.setWindowTitle('Password Generator')
    passWin.setFixedSize(800, 400)

    title = QLabel('Введите имя сайта:')
    passTitle = QLabel('Пароль:')

    nameLine = QLineEdit()

    passwLine = QLineEdit()
    passwLine.setReadOnly(True)

    generButton = QPushButton('Пароль')
    generButton.clicked.connect(generation)

    exitButton = QPushButton('Выход')
    exitButton.clicked.connect(showlog)

    h_line1 = QHBoxLayout()
    h_line1.addWidget(title, alignment = Qt.AlignRight)
    h_line1.addWidget(nameLine, alignment = Qt.AlignLeft)

    h_line2 = QHBoxLayout()
    h_line2.addWidget(exitButton, alignment = Qt.AlignCenter)

    v_line = QVBoxLayout()
    v_line.addLayout(h_line1)
    v_line.addWidget(generButton, alignment = Qt.AlignCenter)
    v_line.addWidget(passTitle, alignment = Qt.AlignCenter)
    v_line.addWidget(passwLine, alignment = Qt.AlignTop)
    v_line.addLayout(h_line2)

    passWin.setLayout(v_line)

    return passWin

def generation():
    webName = nameLine.text()
    alph = 'abcdefghijklmnopqrstuvwxyz1234567890.-'
    webName.lower()
    password = ''
    for i in webName:
        ind = alph.find(i)
        password += logins[login].someshifr[ind]
    passwLine.setText(password)

def showpass():
    passLine.clear()
    errTitle.setText('')
    logWin.hide()
    passWin.show()

class Users():
    def __init__(self, lock, shifr):
        self.somelock = lock
        self.someshifr = shifr

if __name__ == "__main__":
    shifr1 = ['1q','2a', 'zxc', '4x', '5c','V8', '7b', '8n', '9m','_l', 
                '1p', '2o', 'I3', 'u_', '5y', '6t', '7r', '8e', '9w', '0s',
                '1d', '2f', '3g', '4h', '5j', '6k', '_7', '8A', 'Q_', 'G1',
                'LOL', '4F', '5j', '6z', '7p', '8I', '9t', 'QbZ']

    app = QApplication([])

    logins = dict()
    logins1 = getData()
    #print(logins1)
    for k, v in logins1.items():
        logins[k] = Users(v[0], v[1].split())
        # print(k)
        # print(v[0])
        # print(v[1])

    logWin = LOGwindow()
    passWin = PASSwindow()
    checkWin = CHwindow()
    adminWin = ADWindow()
    addWindow = ADDwindow()
    
    logWin.show()
    
    app.exec_()