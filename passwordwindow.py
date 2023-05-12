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
