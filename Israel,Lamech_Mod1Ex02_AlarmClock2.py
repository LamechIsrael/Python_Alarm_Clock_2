

#########################################
# CS 1110A - Programming in Python      #
# Module 1 - Exercise 2 - Alarm Clock 2 #
# Author: Lamech Israel                 #
#                                       #
#########################################

print('Alarm Clock, Part 2')

# Input

current_Time = int(input('\nWhat time is it now (in 24-hour notation):'))

alarm_Hours = int(input('How many hours from now should the alarm go off?'))

# Processing

alarm_Hours *=100
alarm_Days = int(alarm_Hours/2400)
alarm_Remainder = alarm_Hours%2400

alarm_Time = current_Time + alarm_Remainder

if alarm_Time <1200 :
    alarm_Time = '0' + str(alarm_Time)


    
#Output
    

print('The alarm clock will ring',alarm_Days,'days from now at',alarm_Time)

print('\nDone!')
    


