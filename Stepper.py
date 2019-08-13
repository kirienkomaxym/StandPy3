#CURRENT APPLICATION INFO
#200 steps/rev
#12V, 350mA
#Big Easy driver = 1/16 microstep mode


from time import sleep
from math import pi
import RPi.GPIO as gpio #https://pypi.python.org/pypi/RPi.GPIO
#import exitHandler #uncomment this and line 58 if using exitHandler

class stepper:
    #instantiate stepper 
    #pins = [stepPin, directionPin, enablePin]
    def __init__(self, pins):
        #setup pins
        self.pins = pins
        self.stepPin = self.pins[0]
        self.directionPin = self.pins[1]
        self.enablePin = self.pins[2]
        
        #use the broadcom layout for the gpio
        gpio.setmode(gpio.BCM)
        
        #set gpio pins
        gpio.setup(self.stepPin, gpio.OUT)
        gpio.setup(self.directionPin, gpio.OUT)
        gpio.setup(self.enablePin, gpio.OUT)
        
        #set enable to high (i.e. power is NOT going to the motor)
        gpio.output(self.enablePin, True)
        
        #print("Stepper initialized (step=" + self.stepPin + ", direction=" + self.directionPin + ", enable=" + self.enablePin + ")")
    
    #clears GPIO settings
    def cleanGPIO(self):
        gpio.cleanup()
    
    #step the motor
    # steps = number of steps to take
    # dir = direction stepper will move
    # speed = defines the denominator in the waitTime equation: waitTime = 0.000001/speed. As "speed" is increased, the waitTime between steps is lowered
    # stayOn = defines whether or not stepper should stay "on" or not. If stepper will need to receive a new step command immediately, this should be set to "True." Otherwise, it should remain at "False."
    def step(self, steps, dir, speed, stayOn=True):
        #set enable to low (i.e. power IS going to the motor)
        gpio.output(self.enablePin, False)
        
        #set the output to true for left and false for right
        turnLeft = True
        if (dir == 'right'):
            turnLeft = False;
        elif (dir != 'left'):
            print("STEPPER ERROR: no direction supplied")
            return False
        gpio.output(self.directionPin, turnLeft)

        stepCounter = 0
        
        waitTime = 0.01/speed

        while stepCounter < steps:
            #gracefully exit if ctr-c is pressed
            #exitHandler.exitPoint(True) #exitHandler.exitPoint(True, cleanGPIO)

            #turning the gpio on and off tells the easy driver to take one step
            gpio.output(self.stepPin, True)
            gpio.output(self.stepPin, False)
            stepCounter += 1
 
            #wait before taking the next step thus controlling rotation speed
            sleep(waitTime)
        
        if (stayOn == False):
            #set enable to high (i.e. power is NOT going to the motor)
            gpio.output(self.enablePin, True)

        #print("stepperDriver complete (turned " + dir + " " + str(steps) + " steps)")





    #Allow motor to move constant distance with non-changing speed
    #and return back into start. Dia - shaft diameter
    def x_axis_move_main(self, distance, speed, lenght, sleeptime):
        onestepdistance = lenght/200 #distance by 1 step
        stepnumber = distance/onestepdistance

        self.step(stepnumber, "right", speed)
        sleep(sleeptime)

        self.step(stepnumber, "left", speed)



        
    #Allow motor to move dynamic distance with changing  speed
    #list1 - list of distance_value
    #list 2 - list of start values (a, b)
    #dia - shaft diameter
    #sleeptime - time before  turning back
    def y_axis_move_main(self, list1, list2, length, sleeptime):
        x1 = length/200 #distance by 1 step
        global distance
        distance = 10
        global j
        j = 0
        while j < 40:
            stepnumber = int(list1[j])/x1
            speed = 500
            self.step(stepnumber, "right", speed)
            distance += list1[j]
            j+=1
        while distance < 2800:
            stepnumber = int(list1[j])/x1
            speed = list2[j]*50
            #print(speed)
            self.step(stepnumber, "right", speed)
            distance += list1[j]
            j+=1
            #print(distance)
            #print(j)
        sleep(sleeptime)
        self.step(distance/x1, "left", 50)

    def y_axis_move_first(self, list1, list2, list3, length, sleeptime):
        x1 = length/200 #distance by 1 step
        global counter
        counter = 0
        global distance
        distance = 10
        global j
        j = 0
        while j < 40:
            stepnumber = int(list1[j])/x1
            speed = 12
            self.step(stepnumber, "right", speed)
            distance += list1[j]
            j+=1
        while distance < 1000:
            stepnumber = int(list1[j])/x1
            speed = list2[j]*3
            #print(speed)
            self.step(stepnumber, "right", speed)
            distance += list1[j]
            j+=1
            #print(distance)
            #print(j)
        while distance < 1750:
            stepnumber = int(list1[j])/x1
            speed = list3[counter]
            if speed > 0:
                self.step(stepnumber, "right", speed)
            else:
                self.step(stepnumber, "left", (speed*(-1)))
            #print(distance)
            distance += list1[j]
            j+=1
            counter += 1
        sleep(sleeptime)
       #self.step(distance/x1, "left", 50)

    def y_axis_move_second(self, list1, list2, list3, length, sleeptime):
        x1 = length/200 #distance by 1 step
        global counter
        counter = 0
        global distance
        distance = 10
        global j
        j = 0
        while j < 40:
            stepnumber = int(list1[j])/x1
            speed = 12
            self.step(stepnumber, "right", speed)
            distance += list1[j]
            j+=1
        while distance < 1780:
            stepnumber = int(list1[j])/x1
            speed = list2[j]*3
            #print(speed)
            self.step(stepnumber, "right", speed)
            distance += list1[j]
            j+=1
            #print(distance)
            #print(j)
        while distance < 2540:
            stepnumber = int(list1[j])/x1
            speed = list3[counter]
            if speed > 0:
                self.step(stepnumber, "right", speed)
            else:
                self.step(stepnumber, "left", (speed*(-1)))
            #print(speed)
            distance += list1[j]
            #print(distance)
            j+=1
            counter += 1
        sleep(sleeptime)

           
            
            
            
    
gpio.setwarnings(False)





#testStepper = stepper([27,17,22])
#testStepper.x_axis_move(200, 1, 5)
#sleep(5) #vremya v secundax
#testStepper.step(200, "left")
