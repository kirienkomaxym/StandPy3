import sys
from PyQt5 import QtWidgets
from design import design
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
from time import sleep

#import motor running foo, or write here
status_list = [0, 0, 0, 0, 0, 0]

class StandPyGUI(QtWidgets.QMainWindow, design.Ui_StandPy):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.MotorRun)

        self.pushButton_3.setCheckable(True)
        self.pushButton_3.clicked[bool].connect(self.MoveLeft)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.clicked[bool].connect(self.MoveRight)


        self.checkBox.stateChanged.connect(self.StateChecker)
        self.checkBox_2.stateChanged.connect(self.StateChecker_2)
        self.checkBox_3.stateChanged.connect(self.StateChecker_3)
        self.checkBox_4.stateChanged.connect(self.StateChecker_4)
        self.checkBox_5.stateChanged.connect(self.StateChecker_5)
        self.checkBox_6.stateChanged.connect(self.StateChecker_6)



    def StateChecker(self, state):
        if state == Qt.Checked:
            status_list[0] = 1
            print(status_list)


    def StateChecker_2(self, state):
        if state == Qt.Checked:
            status_list[1] = 1
            print(status_list)


    def StateChecker_3(self, state):
        if state == Qt.Checked:
            status_list[2] = 1
            print(status_list)


    def StateChecker_4(self, state):
        if state == Qt.Checked:
            status_list[3] = 1
            print(status_list)


    def StateChecker_5(self, state):
        if state == Qt.Checked:
            status_list[4] = 1
            print(status_list)

    def StateChecker_6(self, state):
        if state == Qt.Checked:
            status_list[5] = 1
            print(status_list)


    def MotorRun(self):
        #Edit function to run a motor
        print('success')
        return None

    def MoveLeft(self, pressed):
        source = self.sender()
        if pressed:
            print('1')
            pressed = 0
        else: print('2')
        #while pressed:
        #    if status_list[0] == True:
        #        print('1')
        #    global StateChecker_2
        #    if StateChecker_2 == True:
        #        print('2')
        #    global StateChecker_3
        #    if StateChecker_3 == True:
        #        print('3')
        #    global StateChecker_4
        #    if StateChecker_4 == True:
        #        print('4')
        #    global StateChecker_5
        #    if StateChecker_5 == True:
        #       print('5')
        #    global StateChecker_6
        #    if StateChecker_6 == True:
        #        print('6')
        #        print('Moved Left')
        #else:
        #    print('emptyness')

    def MoveRight(self, pressed):
        source = self.sender()
        if pressed:
            global StateChecker
            if StateChecker == True:
                print('1')
            global StateChecker_2
            if StateChecker_2 == True:
                print('2')
            global StateChecker_3
            if StateChecker_3 == True:
                print('3')
            global StateChecker_4
            if StateChecker_4 == True:
                print('4')
            global StateChecker_5
            if StateChecker_5 == True:
                print('5')
            global StateChecker_6
            if StateChecker_6 == True:
                print('6')
            print('Moved Left')
        else:
            print('sosiska')

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = StandPyGUI()
    window.show()  #
    app.exec_()


if __name__ == '__main__':
    main()
