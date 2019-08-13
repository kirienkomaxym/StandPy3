This is the code realisation of the Noosphere Stand project.
The project is about showing kids in the Dnipro Planetarium how rockets fly into space, 
user see a GUI on the touchscreen, pushes start button that runs 6 step motors,  which 
is connected to rocket stand. Then user can enjoy a rocket fly.

This realisation is made for RaspberryPi and probably wont work with windows machines, 
venv is needed to run this project lays in the home folder
or you can install needfull things with your hands
To run this app on raspberry you need to:
-have python3+
-install pyqt5(for GUI) with 'pip install pyqt5' and 'pip install pyqt5-tools'
-install RPi.GPIO (if you dont have one) with 'pip install RPi.GPIO'

The main folder consists of:
-ConstantsList.py, file that consist constants of the rocket trajectory, as model of the stand shows real rocket fly, need to have the equation of movement for the every rocket stage. Can be changed to see how rocket fly by the many movement equations

-Stepper.py is the library for the running motors, it has a stepper class and needfull functions

-Main.py is the GUI for this project.It has main start button and two hand-control buttons that is connected to the list of vehicles. If you need to see how it looks like in windows, you can open PoorGui directory that has not-connected with RPi.GPIO gui and run main.pyw
