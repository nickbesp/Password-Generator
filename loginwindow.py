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