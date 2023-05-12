from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QLineEdit, QPushButton, QMessageBox
from random import shuffle
from database import *
from loginwindow import *
from passwordwindow import *
from admin import *

def addUser(login, lock):
    global logins
    shuffle(shifr1)
    logins[login] = Users(lock, shifr1)
    saveData(logins)
    pass
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