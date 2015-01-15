from __future__ import division
import serial
import time
import re
from math import sin as sin
from math import pi as pi


class Nozzle():
    '''This item requires a RS-232 to 485 converter'''
    def __init__(self,port):
        '''Initialization requires that the port number of the 4-port USB to serial
        adapter be input (A,B,C,D) to start. This will be changed to work with different
        computers'''
        self.connection = serial.Serial('/dev/tty.usbserial-FTXE353B'+port)
        self.Opening = str(self.Get_Position())

    def __Send_Command(self,command):
        self.connection.write(command + '\r')
        time.sleep(3.5)

    def __Receive_Data(self,command):
        '''This sends a command to the baratron and returns a value if good, or -1 if
        a time out situation'''
        while True:
            self.connection.write(command + '\r')
            out = ''
            time.sleep(0.1)
            t = time.time()
            while self.connection.inWaiting() >0:
                incoming  = self.connection.read()
                out+=incoming
                if time.time()-t >30:
                    return -1
            return out

    def __Convert_To_mm(self,input):
        '''This function takes the absolute position of the motor and
        converts it into the width of the nozzle opening in mm'''
        mm = 2.55*sin(input*pi/(2*(12500)))+2.55
        return mm

    def Move(self,Input):
        '''This function takes the width of the desired nozzle opening, converts
        it into an absolute position of the stepper motor and then sends the move command
        to the motor'''
        count = 0
        x = -12501 #starting value for x, represents the minimum position
        y = 2.55*sin(x*pi/(2*(12500)))+2.55 #starting y value on the sign curve
        O = Input/((y+Input)/2) #starting error

        while O >= 1:
            x+=1
            y = 2.55*sin(x*pi/(2*(12500)))+2.55
            O = Input/((y+Input)/2)
            count+=1

            if count >50000:
                return -1

        print 'x = ' +str(x)
        self.__Receive_Data('MA '+str(x))

        Desired_Position = str(Input)[0:3]
        Current_Position = self.Get_Position()[0:3]

        #This loop continually asks the motor for its position. When the position
        #of the motor is equal to that of the input, the loop breaks and the function
        #returns 0. Keeps the user from issuing another command until the tool
        #has completed it's move
        count = 0
        while Desired_Position != Current_Position:
            time.sleep(0.3)
            Current_Position = self.Get_Position()[0:3]
            count +=1
            if count > 50:
                return -1
        self.Opening = str(Current_Position)
        return 0

    def Home(self):
        '''Sends the Home Command'''
        self.__Receive_Data('HM 1')
        self.Opening = str(self.Get_Position())
        return 0

    def Get_Position(self):
        '''Promps the controller for it's absolute position, converts the position
        into the number of mm wide the opening on the nozzle is. Returns a string value'''
        x = self.__Receive_Data('PR P')
        Absolute_Position = float(re.findall(r'-?[0-9].*',x)[0])
        mm_open = self.__Convert_To_mm(Absolute_Position)
        return str(mm_open)


if __name__ == '__main__':
    t = time.time()
    X = Nozzle('A')
    #X.Home()
    input = 4.999
    print X.Move(input)
