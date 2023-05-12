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
    ##deleteButton.clicked.connect(showlogAd)

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
        messWin = QMessageBox()                                 #addTrue
        messWin.setText('Пользователь добавлен!')
        messWin.exec()

    adminWin.show()

def addFalse():
    messWin = QMessageBox()
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

def showCheck():
    passLine.clear()
    errTitle.setText('')
    logWin.hide()
    checkWin.show()

def accessFalse():
    messWin = QMessageBox()
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
