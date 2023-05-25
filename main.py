from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QMessageBox, QSplitter, QTextEdit, QPlainTextEdit, QScrollBar, QFrame
from random import shuffle, randint
from database import *

#Добавление пользователя
def addUser(login, lock):
    global logins

    s = list()
    for i in range(len(shifr1)):
        s.append(shifr1[i])

    new_shifr = do_random_shifr(s)
    
    logins[login] = Users(lock, new_shifr)
    saveData(logins)
    pass

def createPresentableUsersData(logins):
    result = 'num | login | password | shifr \n'
    k = 0
    for login in logins:
        k += 1
        elem = logins[login]
        log = login
        passw = str(elem.somelock)

        shifr_list = elem.someshifr
        shif = str()
        for i in shifr_list:
            shif += i + ' '
        
        result += f' {k}   |  {log}  |  {passw}  |  {shif} \n'

    return result

#Создание рандомного шифра
def do_random_shifr(s):
    length = len(s)
    shifr_1 = list()

    for i in range(length):
        shifr_1.append(s[i])

    for i in range(length):
        ind = randint(0, len(s) - 1)
        shifr_1[i] = s[ind]
        s.pop(ind)

    return shifr_1

#Окно администратора
def ADWindow():
    global usersList

    adWin = QWidget()
    adWin.setWindowTitle('Admin')
    adWin.resize(1000, 1080)

    data = createPresentableUsersData(logins)
    usersList = QPlainTextEdit(data)
    usersList.setSizePolicy(900, 900)
    usersList.setReadOnly(True)

    listSplitter1 = QSplitter(Qt.Vertical)
    listSplitter1.addWidget(usersList)

    addButton = QPushButton('Добавить пользователя')
    addButton.clicked.connect(showaddwin)
    deleteButton = QPushButton('Удалить пользователя')
    deleteButton.clicked.connect(showdelwin)
    backButton = QPushButton('Назад')
    backButton.clicked.connect(showlogAd)

    v_line = QVBoxLayout()
    v_line.addWidget(addButton, alignment=Qt.AlignCenter)
    v_line.addWidget(deleteButton, alignment=Qt.AlignCenter)
    v_line.addWidget(backButton, alignment=Qt.AlignCenter)

    h_line = QHBoxLayout()
    h_line.addWidget(listSplitter1)
    h_line.addLayout(v_line)
    
    adWin.setLayout(h_line)

    return adWin

#Окно проверки админского пароля
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

#Окно для добавления пользователя
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

#Окно для удаления пользователя
def DELwindow():
    global dellog
    delWin = QWidget()

    dellog = QLineEdit()
    dellog.setPlaceholderText('Логин')

    confButton = QPushButton('Подтвердить')
    confButton.clicked.connect(delUserAd)

    v_line = QVBoxLayout()
    v_line.addWidget(dellog, alignment=Qt.AlignCenter)
    v_line.addWidget(confButton, alignment=Qt.AlignCenter)

    delWin.setLayout(v_line)

    return delWin

#Удаление пользователя
def delUserAd():
    log = dellog.text()
    dellog.clear()

    if log in logins:
        del logins[log]
        saveData(logins)
        messageBox('Completed', 'Пользователь удален!')
        usersList.setPlainText(createPresentableUsersData(logins))
        delWindow.hide()

    else:
        messageBox('Error', 'Пользователь не найден!')

def messageBox(title, text):
    messWin = QMessageBox()
    messWin.setWindowTitle(title)                                 #addTrue
    messWin.setText(text)
    messWin.exec()

#Добавление пользователя от имнеи админа
def addUserAd():
    global newLogin, newPassword, logins

    log = newLogin.text()
    pas = newPassword.text()
    newLogin.clear()
    newPassword.clear()

    if log in logins:
        messageBox('Error', 'Пользователь уже существует!')
    elif len(log) == 0 or len(pas) == 0:
        messageBox('Error', 'Логин и пароль должны быть заполнены!')
    else:
        addUser(log, pas)
        messageBox('Completed', 'Пользователь добавлен!')
        usersList.setPlainText(createPresentableUsersData(logins))

        addWindow.hide()

def adCheck():
    currPass = userPassword.text()
    userPassword.clear()
    checkWin.hide()
    if currPass == '1234 ':
        data = createPresentableUsersData(logins)
        usersList.setPlainText(data)
        adminWin.show()
    else:
        messageBox('Error', 'Доступ запрещен!')
        logWin.show()

def showaddwin():
    addWindow.show()

def showdelwin():
    delWindow.show()

def showlogAd():
    adminWin.hide()
    logWin.show()

#Главное окно
def LOGwindow():
    global logLine, passLine, errTitle

    logWin = QWidget()
    logWin.setWindowTitle('Password Generator')
    logWin.setFixedSize(400, 200)

    title = QLabel('Добро пожаловать! Введите свой логин и пароль!')
    logtitle = QLabel('Логин:')
    passtitle = QLabel('Пароль:')

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

    logWin.setLayout(v_line)

    return logWin

def showlog():
    logLine.clear()
    passwLine.clear()
    passWin.hide()
    logWin.show()
    nameLine.clear()

#Проверка логина и пароля пользователя
def logCheck():
    global login, lock
    login = logLine.text()
    lock = passLine.text()
    if login in logins:
        if not logins[login].somelock == lock:
            messageBox('Error', 'Неправильный логин или пароль!')
        else:
            showpass()
    elif login == '' or lock == '':
        messageBox('Error', 'Логин и пароль обязательно должны быть заполненными!')
    else:
        addUser(login, lock)
        showpass()

def showCheck():
    passLine.clear()
    logWin.hide()
    checkWin.show()

#Окно генерации паролей
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
    generButton.clicked.connect(generate)

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

#Генерация пароля
def generate():
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
    for k, v in logins1.items():
        logins[k] = Users(v[0], v[1].split())

    logWin = LOGwindow()
    passWin = PASSwindow()
    checkWin = CHwindow()
    adminWin = ADWindow()
    addWindow = ADDwindow()
    delWindow = DELwindow()
    
    logWin.show()
    
    app.exec_()