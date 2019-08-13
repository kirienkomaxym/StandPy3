import sys
from PyQt5 import QtWidgets
from design import design
from PyQt5.QtWidgets import QWidget, QCheckBox, QApplication
from PyQt5.QtCore import Qt
from time import sleep
from threading import Thread
from Stepper import stepper
import ConstantsList


#define ports of the steppers


status_list = [0, 0, 0, 0, 0, 0]



class StandPyGUI(QtWidgets.QMainWindow, design.Ui_StandPy):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.RocketFly)

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


    #StateCheckers connect functions
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
            
    #MotorRunning functions for Threading
    def x_axis_move_main():
        x_axis_main_stepper.x_axis_move_main(3800, 0.000080, 60, 10)
    def x_axis_move_first():
        x_axis_first_stepper.x_axis_move_main(1760, 0.000080, 60, 10)
    def x_axis_move_second():
        x_axis_second_stepper.x_axis_move_main(3000, 0.000080, 60, 10)

    def y_axis_move_main():
        y_axis_main_stepper.y_axis_move_main(distance_list_main, speed_list_main, 60, 10)
    def y_axis_move_first():
        y_axis_main_stepper.y_axis_move_main(distance_list_main, speed_list_first, 60, 10)
    def y_axis_move_second():
        y_axis_main_stepper.y_axis_move_main(distance_list_main, speed_list_second, 60, 10)    

    #MainFoo that run 6 motors by the trajectory    
    def RocketFly(self):      
        Thread(target = x_axis_move_main).start()
        Thread(target = x_axis_move_first).start()
        Thread(target = x_axis_move_second).start()
        Thread(target = y_axis_move_main).start()
        Thread(target = y_axis_move_first).start()
        Thread(target = y_axis_move_second).start()


    #foo for the hand control of the motors
    #takes argumets from the status list
    #status list filled with checkboxes    
    def MoveLeft(self, pressed):
        source = self.sender()
        while pressed:

            if status_list[0] == True:
                x_axis_main_stepper.step(200, "left", 0.000060)
                sleep(1)
                pressed = 0
            if status_list[1] == True:
                x_axis_first_stepper.step(200, "left", 0.000060)
                sleep(1)
                pressed = 0
            if status_list[2] == True:
                x_axis_second_stepper.step(200, "left", 0.000060)
                sleep(1)
                pressed = 0
            if status_list[3] == True:
                y_axis_main_stepper.step(200, "left", 0.000060)
                sleep(1)
                pressed = 0
            if status_list[4] == True:
                y_axis_first_stepper.step(200, "left", 0.000060)
                sleep(1)
                pressed = 0
            if status_list[5] == True:
                y_axis_second_stepper.step(200, "left", 0.000060)
                sleep(1)
                pressed = 0
            status_list = [0, 0, 0, 0, 0, 0]

    #same to moveleft with changed move direction
    def MoveRight(self, pressed):
        source = self.sender()
        while pressed:

            if status_list[0] == True:
                x_axis_main_stepper.step(200, "right", 0.000060)
                sleep(1)
                pressed = 0
            if status_list[1] == True:
                x_axis_first_stepper.step(200, "right", 0.000060)
                sleep(1)
                pressed = 0
            if status_list[2] == True:
                x_axis_second_stepper.step(200, "right", 0.000060)
                sleep(1)
                pressed = 0
            if status_list[3] == True:
                y_axis_main_stepper.step(200, "right", 0.000060)
                sleep(1)
                pressed = 0
            if status_list[4] == True:
                y_axis_first_stepper.step(200, "right", 0.000060)
                sleep(1)
                pressed = 0
            if status_list[5] == True:
                y_axis_second_stepper.step(200, "right", 0.000060)
                sleep(1)
                pressed = 0
            status_list = [0, 0, 0, 0, 0, 0]

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = StandPyGUI()
    window.show()  #
    app.exec_()


if __name__ == '__main__':
    main()
