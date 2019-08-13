from Stepper import stepper
from math import pi

#define ports of the steppers
x_axis_main_stepper = stepper([27, 17, 22])
x_axis_first_stepper = stepper([11, 9, 22])
x_axis_second_stepper = stepper([14, 11, 22])
y_axis_main_stepper = stepper([7, 3, 22])
y_axis_first_stepper = stepper([19, 23, 22])
y_axis_second_stepper = stepper([18, 21, 22])

#define the constants of the trajectory
P0 = [-8.249*(10**5), -0.912] #(a, b)
P1 = [-1.6*(10**(-8)), 8.076*(10**(-5)), -0.1554, 134.7] #Parameters for the 1st stage
P2 = [-5.578*(10**(-12)), 6.007*(10**(-8)),
      -258.1*(10**(-6)), 0.5524, -588, 2.551*(10**5)] #Parameters for the 2nd stage

#Creating coordinate lists
distance_list_main = [10 for i in range(0, 279)]
coordinate_list_main = [i for i in range(10, 2800, 10)]
coordinate_list_first = [i for i in range(1000, 1760, 10)]
coordinate_list_second = [i for i in range(1780, 3000, 10)]

#Creating speed lists
speed_list_main = [P0[0]*P0[1]*0.5*(i**(P0[1]-1)) for i in coordinate_list_main]
speed_list_first = [(4*P1[0]*(i**3)+3*P1[1]*(i**2)+2*P1
                    [2]*i + P1[3]) for i in coordinate_list_first]
speed_list_second = [(5*P2[0]*(i**4) + 4*P2[1]*(i**3) + 3*P2[2]*(i**2)
                      +2*P2[3]*i + P2[4]) for i in coordinate_list_second]

